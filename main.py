def show_menu():
    print("\n=== 수학 공식 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")


def main():
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