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


def get_number(prompt, minimum, maximum):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("입력한 내용이 없습니다. 번호를 입력해주세요.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("숫자로 입력해주세요.")
            continue

        if number < minimum or number > maximum:
            print(f"{minimum}부터 {maximum}까지의 번호를 입력해주세요.")
            continue

        return number


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()

    def show_menu(self):
        print("\n=== 수학 공식 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n--- 문제 {number} / {len(self.quizzes)} ---")
            quiz.display()

            user_answer = get_number("정답 번호를 입력하세요: ", 1, 4)

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(
            f"\n퀴즈 완료! {len(self.quizzes)}문제 중 "
            f"{score}문제를 맞혔습니다."
        )

    def run(self):
        print(f"기본 퀴즈 {len(self.quizzes)}개를 준비했습니다.")

        try:
            while True:
                self.show_menu()
                choice = get_number("메뉴 번호를 입력하세요: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
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


if __name__ == "__main__":
    game = QuizGame()
    game.run()