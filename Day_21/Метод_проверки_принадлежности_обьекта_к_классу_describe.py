# Метод проверики принадлежности обьекта к классу describe()

class Human:
    kg = 50

    def __init__(self):
        print("An object has been created.")
        #pass

    def describe(self):
        print(f"Class: {self.__class__.__name__}")


class Cook(Human):
    def cook(self):
        print("I can to cook.")


class Confectioner(Cook):
    def bake(self):
        print("I can to bake.")


# run
# создание экземпляра класса
Anton = Cook()
# метод класса Cook()
Anton.cook()

# создание экземпляра класса
Yuri = Confectioner()
# метод класса Confectioner()
Yuri.bake()

# свойство класса родителя Human()
print(f"Anton's weight is {Anton.kg} kilograms.")
Yuri.kg = 80 # присваивание нового значения
print(f"Yuri's weight is {Yuri.kg} kilograms.")

# Метод describe(), позволяющий проверить принадлежность обьекта к классу
Anton.describe() # OUT: Класс: Cook
Yuri.describe() # OUT: Класс: Confectioner

'''OUT
An object has been created.
I can to cook.
An object has been created.
I can to bake.
Anton's weight is 50 kilograms.
Yuri's weight is 80 kilograms.
Class: Cook
Class: Confectioner
'''
