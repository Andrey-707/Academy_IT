# Напишите программу, которая получает от пользователя число и выводит обратный отсчет.
# Программа-детонатор.

import time # для установки паузы используем sleep()

from rich import print # для удобства визуализации


running = True
while running:
    try:
        x = int(input("Введите количество секунд: "))
        if x > 0:
            # обратная числовая последовательность от x до 0 не включительно
            for i in range(x, 0, -1):
                print(i)
                # пауза 1 сек
                time.sleep(1)
            print("Boom !\n")
            running = False
        else:
            print("Введите число больше нуля.")
    except ValueError:
        print("ValueError! Введите число.")
