# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ.

# Множественное наследование - это возможность класса иметь более одного родительского класса. При
# множественном наследовании дочерний класс наследует все свойства родительских классов. Механизм
# множественного наследования позволяет вызывать в производном классе методы разных базовых классов,
# от которых он наследуется.

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


# МНОГОУРОВНЕВОЕ НАСЛЕДОВАНИЕ.

# Мы также можем наследовать класс от уже наследуемого. Это называется многоуровневым наследованием.
# Оно может иметь сколько угодно уровней.

# В многоуровневом наследовании свойства родительского класса и наследуемого от него класса передаются
# новому наследуемому классу.

# Класс Derived1 наследуется от класса Base, а класс Derived2 — от класса Derived1.

class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Derived1):
    pass
