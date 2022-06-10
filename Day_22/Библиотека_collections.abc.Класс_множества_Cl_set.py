# Библиотека_collections.abc.Класс_Cl_set

import collections.abc
# from  abc import ABC, abstractmethod

class Cl_set(collections.abc.Set):

    def __init__(self, iterable):
        self.elements = []
        for i in iterable:
            if i not in self.elements:
                self.elements.append(i)

    def __contains__(self, item):
        """
        Magic method. Возвращает item внутри self.elements.
        """
        return item in self.elements

    def __iter__(self):
        """
        Magic method. Возвращает итерацию.
        """
        return iter(self.elements)

    def __len__(self):
        """
        Magic method. Возвращает длину.
        """
        return len(self.elements)

    # НЕ ОБЯЗАТЕЛЬНЫЙ МЕТОД ДЛЯ ВЫВОДА print(s1) или print(s2)
    def __str__(self):
        """
        Magic method. Форматирует вывод информации в консоль.
        """
        return '{'+" ".join([str(i) for i in self.elements]) + "}"


s1 = Cl_set([1, 2, 3])
# ЕСЛИ НЕ ПРОПИСАНЫ МЕТОДЫ __contains__, __iter__, __len__, программа вылетает с ошибкой:
# TypeError: Can't instantiate abstract class Cl_set with abstract methods __contains__, __iter__, __len__

# когдам методы прописаны, можно выводить на экран
print(s1) # OUT: {1 2 3}

s2 = Cl_set([1, 5, 8])
print(s2) # OUT: {1 5 8}

# Сумма не работает!!!
# OUT: TypeError: unsupported operand type(s) for +: 'Cl_set' and 'Cl_set'
# print(s1 + s2)

# Разность
print(s1 - s2) # OUT: {2 3}

# Пересечение
print(s1 & s2) # OUT: {1}

# Обьединение (ЭТО НЕ СУММА, это уникальные элементы)
print(s1 | s2) # OUT: {1 2 3 5 8}
