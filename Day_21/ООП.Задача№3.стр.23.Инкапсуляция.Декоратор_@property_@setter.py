# Задача№3.стр.23.Инкапсуляция,декоратор_property_setter.
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное кол-во килограмм,
# а с помощью метода to_pounds() они переводятся в фунты. ЧТобы закрыть дотуп к переменной "kg" она
# реализовала методы set_kg() - для задания нового значения килограммов, get_kg() - для вывода
# текущего значения kg. Из-за этого возникло неудобство: нам нужно теперь использовать эти два метода
# для задания и вывода значений. Помогите ей переделать класс с использованием функции property() и
# свойств-декораторов. Код приведен ниже.

# CODE
"""
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205


    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")

    def get_kg(self):
        return self.__kg
"""

# Решение:
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    # Декоратор @property позволяет вызывать функцию без скобок (возвращает объект-дескриптор)
    @property
    def kg(self):
        return self.__kg # можно применить увеличение значения, например return self.__kg + 1000

    # Декоратор @.setter используется при записи свойств класса как обычных атрибутов (полей) класса.
    # @.setter работает ТОЛЬКО, если существует @property и применяется к функции, декорированной @property
    # (имена функций должны совпадать)
    @kg.setter
    def kg(self, new_kg):
        self.__kg = new_kg


# создаем экземпляр класса KgToPounds
weight = KgToPounds(10)
print(weight.to_pounds(), "pounds")

# Декоратор @property позволяет вызывать метод kg() без скобок, т.е. позволяет обращаться как-будто напрямую к обьекту
print(weight.kg, "kg")

# После декорирования функции @kg.setter можно обойти инкапсуляцию и присвоить __kg новое значение
weight.kg = 1
print(weight.kg, "kg")
