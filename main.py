import json
import os
import random


class Quiz:
    
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def show(self, number):
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @staticmethod
    def from_dict(data):
        return Quiz(
            data["question"],
            data["choices"],
            data["answer"],
            data.get("hint", ""),
        )
    

STATE_FILE = "state.json"


def create_default_quizzes():
    return [
        Quiz(
            "강아지의 정상 체온은 대략 몇 도일까요?",
            ["36도", "37도", "38~39도", "41도"],
            3,
            "사람 체온보다 조금 높아요.",
        ),
        Quiz(
            "강아지에게 먹이면 위험한 음식은?",
            ["삶은 닭가슴살", "초콜릿", "당근", "오이"],
            2,
            "사람이 좋아하는 달콤한 간식이에요.",
        ),
        Quiz(
            "다 자란 강아지(성견)의 이빨은 보통 몇 개일까요?",
            ["28개", "32개", "42개", "52개"],
            3,
            "사람 어른(32개)보다 많아요.",
        ),
        Quiz(
            "세계에서 가장 빠른 견종으로 알려진 것은?",
            ["푸들", "그레이하운드", "불독", "말티즈"],
            2,
            "경주에 쓰이는 날씬하고 다리가 긴 견종이에요.",
        ),
        Quiz(
            "강아지의 평균 임신 기간은 약 며칠일까요?",
            ["약 30일", "약 63일", "약 90일", "약 120일"],
            2,
            "대략 2개월 정도예요.",
        ),
        Quiz(
            "대한민국 천연기념물 제53호로 지정된 토종 견종은?",
            ["진돗개", "푸들", "비글", "치와와"],
            1,
            "전라남도의 섬 이름이 붙은 견종이에요.",
        ),
    ]


def show_menu():
    print("=" * 40)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 퀴즈 삭제")
    print("6. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        text = input("선택: ").strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 1-6 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-6 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number < 1 or number > 6:
            print("⚠️ 잘못된 입력입니다. 1-6 사이의 숫자를 입력하세요.")
            continue

        return number


def get_answer_choice():
    while True:
        text = input("정답 입력: ").strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number < 1 or number > 4:
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        return number


def get_answer_choice_with_hint(quiz):
    while True:
        text = input("정답 입력 (힌트는 0): ").strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number == 0:
            if quiz.hint == "":
                print("⚠️ 이 문제는 힌트가 없습니다.")
                continue
            return 0
        if number < 1 or number > 4:
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        return number
    

def get_nonempty_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 입력이 비어 있습니다. 다시 입력하세요.")
            continue
        return text


def get_quiz_count(max_count):
    while True:
        text = input(f"풀 문제 수를 입력하세요 (1-{max_count}): ").strip()

        if text == "":
            print(f"⚠️ 입력이 비어 있습니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print(f"⚠️ 잘못된 입력입니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number < 1 or number > max_count:
            print(f"⚠️ 잘못된 입력입니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        return number

    

def get_quiz_number(message, max_count):
    while True:
        text = input(f"{message} (1-{max_count}): ").strip()

        if text == "":
            print(f"⚠️ 입력이 비어 있습니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print(f"⚠️ 잘못된 입력입니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number < 1 or number > max_count:
            print(f"⚠️ 잘못된 입력입니다. 1-{max_count} 사이의 숫자를 입력하세요.")
            continue

        return number

    
class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.load_state()


    def load_state(self):
        if not os.path.exists(STATE_FILE):
            return  # 첫 실행: 기본 퀴즈 사용

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = data["best_score"]
        except (OSError, ValueError, KeyError, TypeError):
            print("⚠️ 저장 파일이 손상되어 기본 데이터로 초기화합니다.")
            self.save_state()
            return

        self.quizzes = quizzes
        self.best_score = best_score
        score_text = "없음" if best_score is None else f"{best_score['score']}점"
        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score_text})")

        
    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 데이터를 저장하지 못했습니다.")

    
    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        count = get_quiz_count(len(self.quizzes))
        print(f"\n📝 퀴즈를 시작합니다! (총 {count}문제)\n")

        correct_count = 0
        score_points = 0.0
        shuffled_quizzes = random.sample(self.quizzes, count)
        for number, quiz in enumerate(shuffled_quizzes, start=1):
            quiz.show(number)
            used_hint = False
            user_answer = get_answer_choice_with_hint(quiz)
            if user_answer == 0:
                used_hint = True
                print(f"💡 힌트: {quiz.hint}\n")
                user_answer = get_answer_choice()

            if quiz.is_correct(user_answer):
                correct_count += 1
                if used_hint:
                    score_points += 0.5
                    print("✅ 정답입니다! (힌트 사용: 0.5점 처리)\n")
                else:
                    score_points += 1
                    print("✅ 정답입니다!\n")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")

        total = count
        score = int(score_points / total * 100)
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if self.best_score is None or score > self.best_score["score"]:
            self.best_score = {"score": score, "correct": correct_count, "total": total}
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()
        print("=" * 40)


    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")

        question = get_nonempty_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choices.append(get_nonempty_text(f"선택지 {i}: "))

        answer = get_answer_choice()
        hint = input("힌트 (없으면 Enter): ").strip()

        self.quizzes.append(Quiz(question, choices, answer, hint))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def delete_quiz(self):
        if len(self.quizzes) == 0:
            print("⚠️ 삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number = get_quiz_number("삭제할 퀴즈 번호를 입력하세요", len(self.quizzes))

        removed = self.quizzes.pop(number - 1)
        self.save_state()
        print(f"\n🗑️ 삭제되었습니다: {removed.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("\n⚠️ 아직 퀴즈를 풀지 않았습니다.")
            return

        print(f"\n🏆 최고 점수: {self.best_score['score']}점 "
              f"({self.best_score['total']}문제 중 {self.best_score['correct']}문제 정답)")

    def run(self):
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.delete_quiz()
            elif choice == 6:
                self.save_state()
                print("프로그램을 종료합니다. 안녕히 가세요!")
                break


def run():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 중단되었습니다. 데이터를 저장하고 종료합니다.")
        game.save_state()


run()