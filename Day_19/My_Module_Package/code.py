# Сработают все принты кроме последнего. Программа не посчитает площадь квадрата.

from figures import *


# В данном случае программа сработает корректно
print("Длина окружности:", circle_perimeter()) # OUT: 31.416
print("Периметр треугольника:", triangle_perimeter()) # OUT: 17
print("Периметр квадрата:", square_perimeter()) # OUT: 40

# Программа так же посчитает все площиди кроме площади квадрата
print("Площадь круга:", circle_area()) # OUT: 78.54
print("Площадь треугольника:", triangle_area()) # OUT: 18.767 

# В данном случае программа выходит с исключением NameError по причине того, что в файле __ini__.py
# в figures список __all__ = [] не содержит функцию square_area()
print("Площадь квадрата:", square_area()) # OUT: NameError: name 'square_area' is not defined
