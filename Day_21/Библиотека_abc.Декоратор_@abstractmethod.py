# Библиотека abc. Абстрактный метод. Декоратор @abstractmethod

# Абстрактный класс – класс, содержащий один и более абстрактных методов.

# Абстрактный метод – метод, который объявлен, но не реализован.

# Абстрактный класс не может быть инстанциирован (создан его экземпляр). Нужно наследовать этот
# класс и реализовать (переопределить) все абстрактные методы, и только после этого можно создавать
# экземпляры такого наследника.

from abc import ABC, abstractmethod


class Shape(ABC):

    def info(self):
        print(f"Периметр: {self.per()} \n"
              f"Площадь: {self.area()}")

    @abstractmethod
    def area(self):
        return None

    @abstractmethod
    def per(self):
        return None


class Rectangle(Shape):

    def area(self):
        return None
        
    def per(self):
        return None


class Square(Rectangle, Shape):
    pass


# run
# при попытке создать экземпляр класса Shape
# s = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area, per

# экземпляр класса Rectangle и Square создаются (наследуются) без ошибок
r = Rectangle()
sq = Square()
