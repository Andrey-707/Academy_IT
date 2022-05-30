# Задача2.стр.41. Равенство трех заданных чисел.

# Напишите программу Python для трех заданных чисел 'x', 'y', 'z'. Однако, если два значения равны,
# сумма будет равна нулю, например если x == y или x == z, то сумма равна нулю.

from rich import print # выделение чисел в строке вывода


while True:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            x = int(input("Введите число 'x': "))
            y = int(input("Введите число 'y': "))
            z = int(input("Введите число 'z': "))
            if x == y or x == z or y == z:
                result = 0
                print(f"Два значения равны, сумма будет равна {result}.")
            else:
                result = sum([x, y, z])
                print(f"Числа не равны, их сумма равна {result}.")
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите число.")
