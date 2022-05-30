# Задача5.стр.41. Сумма двух чисел. Присвоение значения.

# Напишите программу Python для нахождения суммы двух заданных чисел. Однако, если сумма попадает в
# диапазон от 15 до 20, она должна вернуть 20.

def sum_double(x, y):
    '''Функция вычисления суммы двух чисел'''
    result = sum([x, y])
    if result in range(15, 21):
        result = float(20)
    return result


while True:
    try:
        # программа зациклена, для выхода ввести n
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            print(f"Сумма равна {sum_double(x, y)}.")
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Вы ввели не число.")
