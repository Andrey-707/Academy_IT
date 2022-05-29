# Напишите программу, которая загадывает число от 1 до 10. Выполнять программу до тех пор пока пользователь
# не угадает число.

import random # для создания рандомного числа

from rich import print # для удобства визуализации


running = True
number = random.randint(0, 10)

while running:
    try:
        n = int(input("Угадайте число от 0 до 10\n"))
        if number < n:
            print("Загаданное число меньше.")
        elif number > n:
            print("Загаданное число больше.")
        else:
            print("Верно! Загаданное число", number)
            running = False
    except ValueError:
        print("ValueError! Введите число.")
