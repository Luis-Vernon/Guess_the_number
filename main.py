from game import GuessGame
from stats import load_best, save_best

def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1 - Лёгкий (1–50)")
    print("2 - Средний (1–100)")
    print("3 - Сложный (1–200)")
    while True:
        choice = input("Ваш выбор (1/2/3): ")
        if choice == '1':
            return 1, 50
        elif choice == '2':
            return 1, 100
        elif choice == '3':
            return 1, 200
        else:
            print("Некорректный ввод, попробуйте снова.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    best = load_best()
    if best is not None:
        print(f"Текущий рекорд: {best} попыток")
    else:
        print("Рекордов пока нет.")

    min_num, max_num = choose_difficulty()
    game = GuessGame(min_num, max_num)
    print(f"Загадано число от {min_num} до {max_num}.")

    while True:
        try:
            user_input = input("Введите число (или 'q' для выхода): ")
            if user_input.lower() == 'q':
                print("До свидания!")
                break
            num = int(user_input)
            result = game.guess(num)
            if result == -1:
                print("Загаданное число БОЛЬШЕ.")
            elif result == 1:
                print("Загаданное число МЕНЬШЕ.")
            else:
                print(f"Поздравляю! Вы угадали за {game.attempts} попыток.")
                if best is None or game.attempts < best:
                    print("🎉 Новый рекорд!")
                    save_best(game.attempts)
                    best = game.attempts
                # Начинаем новую игру с тем же уровнем сложности
                game.reset(min_num, max_num)
                print(f"Загадано новое число от {min_num} до {max_num}. Попробуйте ещё раз!")
        except ValueError:
            print("Ошибка: введите целое число или 'q'.")

if __name__ == "__main__":
    main()