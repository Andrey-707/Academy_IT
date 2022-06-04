# Задача№2.стр.27.Построить_треугольник.
# Николаю ребуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. Для этого он
# решил создать класс TriangleChecker, принимающий только положительные числа.

# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):

# - Можно постоить треугольник!
# - С отрицательными числами ничего не выйдет.
# - Нужно вводить только числа.
# - Из этого треугольник не постоить.


# Реализация:
class Triangle():
    def __init__(self, a, b, c):
        '''Magic method. Initialization object'''
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        '''Checks for the possibility of constructing a triangle'''
        if (isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int)) and \
        (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a) and \
        (self.a > 0 and self.b > 0 and self.c > 0):
            print("Можно постоить треугольник!")
        elif not (isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int)):
            print("Нужно вводить только числа.")
        elif (isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int)) and \
        (self.a < 0 or self.b < 0 or self.c < 0):
            print("С отрицательными числами ничего не выйдет.")
        else:
            print("Треугольник не постоить.")


# run
# Случай, когда треуголник можно постоить (выполняется условие if)
triangle1 = Triangle(4, 3, 5)
triangle1.is_triangle() # OUT: Можно постоить треугольник!

# Случай, когда треуголник нельзя постоить (выполняется первое условие elif)
triangle2 = Triangle(4, -3, 5)
triangle2.is_triangle() # OUT: С отрицательными числами ничего не выйдет.

# Случай, когда треуголник нельзя постоить (выполняется второе условие elif)
triangle3 = Triangle(4, "три", 5)
triangle3.is_triangle() # OUT: Нужно вводить только числа.

# Случай, когда треуголник нельзя постоить (выполняется условие else)
triangle4 = Triangle(4, 1, 5)
triangle4.is_triangle() # OUT: Треугольник не постоить.
