class Quiz:
    
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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
    

def create_default_quizzes():
    return [
        Quiz(
            "강아지의 정상 체온은 대략 몇 도일까요?",
            ["36도", "37도", "38~39도", "41도"],
            3,
        ),
        Quiz(
            "강아지에게 먹이면 위험한 음식은?",
            ["삶은 닭가슴살", "초콜릿", "당근", "오이"],
            2,
        ),
        Quiz(
            "다 자란 강아지(성견)의 이빨은 보통 몇 개일까요?",
            ["28개", "32개", "42개", "52개"],
            3,
        ),
        Quiz(
            "세계에서 가장 빠른 견종으로 알려진 것은?",
            ["푸들", "그레이하운드", "불독", "말티즈"],
            2,
        ),
        Quiz(
            "강아지의 평균 임신 기간은 약 며칠일까요?",
            ["약 30일", "약 63일", "약 90일", "약 120일"],
            2,
        ),
        Quiz(
            "대한민국 천연기념물 제53호로 지정된 토종 견종은?",
            ["진돗개", "푸들", "비글", "치와와"],
            1,
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
    print("5. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        text = input("선택: ").strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        if not text.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        number = int(text)
        if number < 1 or number > 5:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
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


def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)\n")

    correct_count = 0
    for number, quiz in enumerate(quizzes, start=1):
        quiz.show(number)
        user_answer = get_answer_choice()

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!\n")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")

    score = int(correct_count / len(quizzes) * 100)
    print("=" * 40)
    print(f"🏆 결과: {len(quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)


def show_quiz_list(quizzes):
    if len(quizzes) == 0:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)\n")
    print("-" * 40)
    for number, quiz in enumerate(quizzes, start=1):
        print(f"[{number}] {quiz.question}")
    print("-" * 40)


def get_nonempty_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 입력이 비어 있습니다. 다시 입력하세요.")
            continue
        return text


def add_quiz(quizzes):
    print("\n📌 새로운 퀴즈를 추가합니다.\n")

    question = get_nonempty_text("문제를 입력하세요: ")

    choices = []
    for i in range(1, 5):
        choice = get_nonempty_text(f"선택지 {i}: ")
        choices.append(choice)

    answer = get_answer_choice()

    quizzes.append(Quiz(question, choices, answer))
    print("\n✅ 퀴즈가 추가되었습니다!")
    

def main():
    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            add_quiz(quizzes)
        elif choice == 3:
            show_quiz_list(quizzes)
        elif choice == 5:
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print(f"{choice}번 기능은 아직 준비 중입니다.")


def run():
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 중단되었습니다. 안전하게 종료합니다.")


run()