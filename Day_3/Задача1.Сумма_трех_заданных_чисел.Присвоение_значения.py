# Задача1.стр.41. Сумма трех заданных чисел. Присвоение_значения.

# Напишите программу Python для вычисления суммы трех заданных чисел, если значения равны, верните 
# трехкратную их сумму, т.е. их сумму, увеличенную в три раза.

from rich import print # выделение чисел в строке вывода


while True:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            a = int(input("Введите число 'a': "))
            b = int(input("Введите число 'b': "))
            c = int(input("Введите число 'c': "))
            if a == b == c:
                result = sum([a, b, c]) * 3
                print(f"Числа равны, их трехкратная сумма равна {result}.")
            else:
                result = sum([a, b, c])
                print(f"Числа не равны, их сумма равна {result}.")
        elif escape == "n":
            print("Выход из программы.")         
            break
        else:
            print("Некорректный ввод. Введите y/n")             
    except ValueError:
        print("ValueError! Введите число.")