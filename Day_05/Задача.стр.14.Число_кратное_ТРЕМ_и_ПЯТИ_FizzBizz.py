# Напишите программу Python, которая выполняет перебор целых чисел от 1 до 50. Для кратных трем выведите
# "Fizz" вместо числа, а для кратных пяти выведите "Buzz".
# Для чисел, кратных трем и пяти, выведите "FizzBizz"


import time # для установки паузы используем функцию sleep()

from rich import print # для удобства визуализации


for i in range(1, 50+1):
    if i % 3 == 0 and i % 5 == 0:
        time.sleep(1)
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        time.sleep(1)
        print(i, "Fizz")
    elif i % 5 == 0:
        time.sleep(1)
        print(i, "Buzz")
    else:
        # остальные случаи пропускаем
        pass
