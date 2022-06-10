# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ.

# Множественное наследование - это способность наследоваться сразу от нескольких классов. Такой механизм
# позволяет вызывать в производном классе методы разлых базовых классов, от которых он наследуется.

# Пример:

class Base1:

    def tic(self):
        return "TIC"


class Base2:

    def tac(self):
        return "TAC"


class Base3:

    def toe(slef):
        return "TOE"


class Derived(Base1, Base2, Base3):
    pass


# run
A = Derived()
print(A.tic(), A.tac(), A.toe(), end=" ") # OUT: TIC TAC TOE
