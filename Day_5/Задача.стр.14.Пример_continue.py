# Напишите программу, которая печатает все числа от 0 до 6, кроме 3 и 6.

from rich import print # для удобства визуализации


for i in range(0, 7):
    if i != 3 and i != 6:
        print(i)
    else:
        #print("Число", i, "пропускаем")
        continue
