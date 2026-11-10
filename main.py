import json
from pathlib import Path


STATE_FILE = Path(__file__).resolve().parent / "state.json"


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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


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


def get_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("내용이 비어 있습니다. 다시 입력해주세요.")
            continue

        return text


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.load_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        try:
            with STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        except OSError as error:
            print(f"파일을 저장하지 못했습니다: {error}")
            return False

        return True

    def load_state(self):
        try:
            with STATE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

            quiz_data = data["quizzes"]
            best_score = data["best_score"]

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            if best_score is not None:
                if type(best_score) is not int or best_score < 0:
                    raise ValueError("최고 점수 형식이 올바르지 않습니다.")

            loaded_quizzes = []

            for item in quiz_data:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 형식이 올바르지 않습니다.")

                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not isinstance(question, str) or not question.strip():
                    raise ValueError("문제가 비어 있거나 형식이 잘못되었습니다.")

                if not isinstance(choices, list) or len(choices) != 4:
                    raise ValueError("선택지는 4개여야 합니다.")

                for choice in choices:
                    if not isinstance(choice, str) or not choice.strip():
                        raise ValueError("선택지가 비어 있거나 형식이 잘못되었습니다.")

                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답 번호는 1부터 4까지여야 합니다.")

                loaded_quizzes.append(Quiz(question, choices, answer))

            self.quizzes = loaded_quizzes
            self.best_score = best_score
            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
        except (ValueError, KeyError, UnicodeError) as error:
            print(f"저장 파일이 손상되어 기본 데이터로 시작합니다: {error}")
        except OSError as error:
            print(f"파일을 읽지 못해 기본 데이터로 시작합니다: {error}")

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

    def add_quiz(self):
        print("\n=== 새 퀴즈 추가 ===")

        question = get_text("문제를 입력하세요: ")
        choices = []

        for number in range(1, 5):
            choice = get_text(f"선택지 {number}을 입력하세요: ")
            choices.append(choice)

        answer = get_number("정답 번호를 입력하세요: ", 1, 4)

        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)

        print(f"퀴즈가 추가되었습니다. 현재 총 {len(self.quizzes)}개입니다.")

        if self.save_state():
            print("state.json에 저장했습니다.")
        else:
            print("추가한 퀴즈는 현재 실행 중인 게임에만 반영되었습니다.")

    def show_quizzes(self):
        print("\n=== 퀴즈 목록 ===")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈는 총 {len(self.quizzes)}개입니다.")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n--- 퀴즈 {number} ---")
            quiz.display()
            print(f"정답: {quiz.answer}번")

    def run(self):
        print(f"퀴즈 {len(self.quizzes)}개를 준비했습니다.")

        try:
            while True:
                self.show_menu()
                choice = get_number("메뉴 번호를 입력하세요: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quizzes()
                elif choice == 4:
                    print("최고 점수 확인을 선택했습니다.")
                elif choice == 5:
                    print("게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 안전하게 종료합니다.")
        finally:
            self.save_state()


if __name__ == "__main__":
    game = QuizGame()
    game.run()