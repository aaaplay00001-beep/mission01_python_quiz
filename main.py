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


def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 5:
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