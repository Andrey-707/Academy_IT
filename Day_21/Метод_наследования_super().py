# Метод_наследования_super()

class Shape:
    def __init__(self):
        print("Фигура создана.")

    def info(self):
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.per()}")


class Rectangle(Shape):
    def __init__(self, a, b):
        # Rectangle наследует конструктор от клсса родителя Shape
        super().__init__()
        # Переопределение (дополнение/коррекция) метода __init__() в производном классе
        print("Я наследник Shape.")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def per(self):
        return self.a*2 + self.b*2


class Square(Rectangle):
    def __init__(self, size):
        # Square наследует конструктор от клсса родителя Rectangle
        super().__init__(size, size) # аргумент size передается в метод __init__ родительского класса
        # Переопределение (дополнение/коррекция) метода __init__() в производном классе
        print("Я наследник Rectangle.")

    # Переопределение (дополнение/коррекция) метода area() в производном классе
    def area(self):
        return self.a ** 2

    # Переопределение (дополнение/коррекция) метода per() в производном классе
    def per(self):
        return 4 * self.a


# run
# создание экземпляра класса Rectangle
r = Rectangle(2, 4)
# метод класса info()
r.info()

'''OUT:
Фигура создана.
Я наследник Shape.
Площадь: 8
Периметр: 12
'''

print() # пустая строка

# создание экземпляра класса Square
sq = Square(3)
# Т.к. Square наследует конструктор от клсса родителя Rectangle, поэтому он имеет обе стороны, равные size
print(f"Сторона a={sq.a}, сторона b={sq.b}")
# метод класса info()
sq.info()

'''OUT:
Фигура создана.
Я наследник Shape.
Я наследник Rectangle.
Сторона a=3, сторона b=3
Площадь: 9
Периметр: 12
'''
