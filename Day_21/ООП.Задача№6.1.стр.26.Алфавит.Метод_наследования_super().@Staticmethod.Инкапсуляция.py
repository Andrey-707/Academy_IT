# Задача№6.стр.26.Алфавит.Метод_наследования_super.Статикметод.Инкапсуляция.

# Есть алфавит, характеристики которого: 1. Язык; 2. Список букв
# Для алфавита нужно:
# 1. Напечатать все буквы алфавита
# 2. Посчитать количество букв

# Так же есть английский алфавит, характеристики которого: 1. Язык; 2. Список букв; 3. Количество букв
# Для английского алфавита можно:
# 1. Посчитать количество букв
# 2. Определить, относится ли буква к английскому алфавиту
# 3. Получить пример текста на английском языке

# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1)lang-язык; 2)letters-список букв.
# Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита.
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите.

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве
# параметров ему будут передаваться обозначение языка (например, 'En') и строка, состоящая из всех букв
# алфавита (можно воспользоваться свойством ascii_uppercase из модуля string)
# 3. Добавьте приватное статическое свойство __letters_num(), который будет хранить количество букв в 
# алфавите.
# 4. Создайте метод is_eng_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе он будет возвращать значение свойства
# __letters_num()
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

# Решение:
import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):

    # 3.Добавьте приватное статическое свойство __letters_num(), который будет хранить количество букв
    # в алфавите
    __letters_num = 26

    # 2.Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В
    # качестве параметров ему будут передаваться обозначение языка (например, 'Eng') и строка, состоящая
    # из всех букв алфавита (можно воспользоваться свойством ascii_uppercase из модуля string)
    def __init__(self):
        # импортирована библиотека string, берутся все буквы "Eng" алфавита в нижнем регистре
        super().__init__("Eng", string.ascii_lowercase)

    # 4.Создайте метод is_eng_letter(), который будет принимать букву в качестве параметра и определять,
    # относится ли эта к буква английскому алфавиту.
    def is_eng_letter(self, letter):
        if letter.lower() in self.letters:
            return True
        return False
    
    # 5.Переопределите метод letters_num() - пусть в текущем классе он будет возвращать значение свойства
    # __letters_num()
    @staticmethod
    def letters_num():
        return EngAlphabet.__letters_num

    # 6.Создайте статический метод example(), который будет возвращать пример текста на английском языке.
    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")


# Создаем экземпляр класса EngAlphabet, родителем которого является Alphabet
E = EngAlphabet()

# Выводим на экран тип языка
print(E.lang) # OUT: Eng

# Выводим на экран ВСЕ буквы английского алфавита
print(E.letters) # OUT: abcdefghijklmnopqrstuvwxyz

# Применим staticmethod letters_num() к экземпляру класса 'E', он выводит количество букв в 'Eng' алфавите
print(E.letters_num()) # OUT: 26

# Выводим на экран bool значение "Это английская буква?"
print(E.is_eng_letter("t")) # OUT: True

# Применим staticmethod example() к экземпляру класса 'E', он выводит на экран пример англейского текста.
# OUT: English Example:
#      Don't judge a book by it's cover.
E.example()


# По аналогии с английским алфавитом сделаем для русского алфавита.
class RusAlphabet(Alphabet):

    # 3.Добавьте приватное статическое свойство __letters_num(), который будет хранить количество букв
    # в алфавите
    __letters_num = 33

    # 2.Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В
    # качестве параметров ему будут передаваться обозначение языка (например, 'Rus') и строка, состоящая
    # из всех букв алфавита
    def __init__(self):
        super().__init__("Rus", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

    # 4.Создайте метод is_rus_letter(), который будет принимать букву в качестве параметра и определять,
    # относится ли эта к буква английскому алфавиту.
    def is_rus_letter(self, letter):
        if letter.lower() in self.letters:
            return True
        return False

    # 5.Переопределите метод letters_num() - пусть в текущем классе он будет возвращать значение свойства
    # __letters_num()
    @staticmethod
    def letters_num():
        return RusAlphabet.__letters_num

    # 6.Создайте статический метод example(), который будет возвращать пример текста на английском языке.
    @staticmethod
    def example():
        print("Русский Пример:\nНе судите о книге по её обложке.")


# Создаем экземпляр класса RusAlphabet, родителем которого является Alphabet
R = RusAlphabet()

# Выводим на экран тип языка
print(R.lang) # OUT: Rus

# Выводим на экран ВСЕ буквы русского алфавита
print(R.letters) # OUT: абвгдеёжзийклмнопрстуфхцчшщъыьэюя

# Применим staticmethod letters_num() к экземпляру класса 'R', он выводит количество букв в 'Rus' алфавите
print(R.letters_num()) # OUT: 33

# Выводим на экран bool значение "Это русская буква?"
print(R.is_rus_letter("я")) # OUT: True

# Применим staticmethod example() к экземпляру класса 'R', он выводит на экран пример русского текста.
# OUT: Русский Пример:
#      Не судите о книге по её обложке.
R.example()
