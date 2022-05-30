# Задача№1.стр.26.Тип данных из input()
# Пользователь ввел некотурую комбинацию чисел. Узнать, какой тип данных имеет то, что он ввел.

from rich import print
from ast import literal_eval


def get_type(input_data):
    '''Функция проверяет какого типа данные, введеннные пользователем'''
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # строка, поэтому возвращаем тип данных str
        return str
#-------------------эти данные вводим в цикле while для проверки типа данных---------------------------------
print("Эти данные вводим в input()")
str_1 = +4
print("'+4' по типу данных является", type(str_1)) # <class 'int'>
str_2 = 47.32
print("'47.32' по типу данных является", type(str_2)) # <class 'float'>
str_3 = "tom"
print("'tom' по типу данных является", type(str_3)) # <class 'str'>
str_4 = -123
print("'-123' по типу данных является", type(str_4)) # <class 'int'>
str_5 = -0.5697
print("'-0.5697' по типу данных является", type(str_5)) # <class 'float'>
str_6 = 3,14
print("'3,14' по типу данных является", type(str_6)) # <class 'tuple'>
str_7 = 0
print("'0' по типу данных является", type(str_7)) # <class 'int'>
str_8 = 5e50
print("'5e50' по типу данных является", type(str_8)) # <class 'float'>
str_9 = .50
print("'.50' по типу данных является", type(str_9)) # <class 'float'>

print() # пустая строка


#--------------------------- Проверка типа данных. Ввод от пользователя -----------------------------------------------
while True:
    input_data = input("Проверка типа данных. Для выхода введите 'end'.\n")

    if input_data == "end":
        print("Выход из программы.")
        break
    else:
        print(get_type(input_data))
