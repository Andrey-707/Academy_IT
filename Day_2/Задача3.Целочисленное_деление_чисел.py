# Задача3.стр.26. Целочисленное деление чисел.

# Проверить делимость одного целого числа на другое
# 1. Пользователь вводит числа 'a' и 'b''
# 2. Если 'a' делится на 'b' без остатка, то число 'a' делится нацело на 'b'
#    Иначе, в остальных случаях, есть остаток и он не равен нулю.
#    Следовательно, 'a' не делится на 'b'.

while True:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            a = int(input("Введите целое число 'a': "))
            b = int(input("Введите целое число 'b': "))         
            if a % b == 0:
                print("Число 'a' делится нацело на 'b'.")
            else:
                print("Число 'a' не делится нацело на 'b'.") 
        elif escape == "n":
            print("Выход из программы.")         
            break
        else:
            print("Некорректный ввод. Введите y/n")             
    except ValueError:
        print("ValueError! Вы ввели не число.")
    except ZeroDivisionError:
        print("ZeroDivisionError! Деление на ноль.")
