# Напишите программу для вычисления суммы и среднего n целых чисел. Числа вводить пользователем до тех пор,
# пока не введет ноль, чтобы закончить.

from rich import print # для удобства визуализации


running = True
summ = 0
while running:
    try:
        enter = int(input("Ввод: "))
        if enter != 0:
            summ += enter
        elif enter == None:
            print("Ошибка ввода данных.")
        else:
            print("Сумма", summ, "\nСреднее значение", summ / 2)
            running = False   
    except ValueError:
        print("ValueError! Введите целое число.")
