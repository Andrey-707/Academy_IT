# Задача3. Площадь круга.

# Напишите программу Python, которая принимает радиус круга от пользователя и вычисляет площадь.
# Площадь круга: S = PI*r**2

import math

PI = math.pi # константа

def area():
    '''Функция расчета площади круга'''
    r = float(input("Введите радиус круга в см: "))
    # откругление до трех цифр после точки
    S = round(PI*r**2, 3)
    return S

print("Площадь круга составляет", area(), "см2")
