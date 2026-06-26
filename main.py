from game import GuessGame
from stats import load_best, save_best

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    best = load_best()
    if best is not None:
        print(f"Текущий рекорд: {best} попыток")
    else:
        print("Рекордов пока нет.")

    game = GuessGame()

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
                # Начинаем новую игру
                game.reset()
                print("Загадано новое число. Попробуйте ещё раз!")
        except ValueError:
            print("Ошибка: введите целое число или 'q'.")

if __name__ == "__main__":
    main()