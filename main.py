class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


def create_default_quizzes():
    return [
        Quiz(
            "직사각형의 넓이를 구하는 공식은?",
            [
                "가로 + 세로",
                "가로 × 세로",
                "(가로 + 세로) × 2",
                "가로 ÷ 세로",
            ],
            2,
        ),
        Quiz(
            "삼각형의 넓이를 구하는 공식은?",
            [
                "밑변 × 높이",
                "(밑변 + 높이) ÷ 2",
                "밑변 × 높이 ÷ 2",
                "밑변 × 높이 × 2",
            ],
            3,
        ),
        Quiz(
            "반지름이 r인 원의 넓이를 구하는 공식은? (π는 원주율)",
            [
                "π × r²",
                "2 × π × r",
                "π × r",
                "2 × π × r²",
            ],
            1,
        ),
        Quiz(
            "사다리꼴의 넓이를 구하는 공식은?",
            [
                "윗변 × 아랫변 × 높이",
                "(윗변 + 아랫변) × 높이",
                "(윗변 + 아랫변) ÷ 높이",
                "(윗변 + 아랫변) × 높이 ÷ 2",
            ],
            4,
        ),
        Quiz(
            "한 모서리의 길이가 a인 정육면체의 부피를 구하는 공식은?",
            [
                "a × a",
                "a × a × a",
                "a × 6",
                "a × 12",
            ],
            2,
        ),
    ]


def show_menu():
    print("\n=== 수학 공식 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")


def main():
    quizzes = create_default_quizzes()
    print(f"기본 퀴즈 {len(quizzes)}개를 준비했습니다.")

    try:
        while True:
            show_menu()
            user_input = input("메뉴 번호를 입력하세요: ").strip()

            if user_input == "":
                print("입력한 내용이 없습니다. 번호를 입력해주세요.")
                continue

            try:
                choice = int(user_input)
            except ValueError:
                print("숫자로 입력해주세요.")
                continue

            if choice < 1 or choice > 5:
                print("1부터 5까지의 번호를 입력해주세요.")
                continue

            if choice == 1:
                print("퀴즈 풀기를 선택했습니다.")
            elif choice == 2:
                print("퀴즈 추가를 선택했습니다.")
            elif choice == 3:
                print("퀴즈 목록을 선택했습니다.")
            elif choice == 4:
                print("최고 점수 확인을 선택했습니다.")
            elif choice == 5:
                print("게임을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 안전하게 종료합니다.")


main()