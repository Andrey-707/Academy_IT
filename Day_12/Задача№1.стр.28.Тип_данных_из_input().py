# Задача№1.стр.28.Тип_данных_из_input().
# Пользователь вводит какие-то символы. Написать три функции:
# is_int() - проверяет, можно ли данные в строке без ошибок преобразовать в тип данных int
# is_float() - ...........................................................в тип данных float
# is_str() - .............................................................в тип данных str

def is_int(s):
    '''Функция проверяет, можно ли данные в строке без ошибок преобразовать тип данных int'''
    if s == "":
        return False
    if s.isdigit():
        return True
    else:
        if s[0] != "+" and s[0] != "-":
            return False
        elif s[1:].isdigit():
            return True
        else:
            return False

s1 = "+56255"
print(is_int(s1))


def is_float(s):
    '''Функция проверяет, можно ли данные в строке без ошибок преобразовать тип данных float'''
    if s == "":
        return False
    if is_int(s):
        return True
    s_s = s.split(".")
    print(s_s)
    if len(s_s) == 2 and (s_s[0] == '' or s_s[0] == '+' or s_s[0] == '-') and s_s[1].isdigit():
        return True
    if len(s_s) == 2 and isint(s_s[0]) and s_s[1].isdigit():
        return True
    s_s = s.split("e")
    print(s_s)
    if len(s_s) == 2 and isint(s_s[0]) and s_s[1].isdigit():
        return True
    return False


s2 = ".50"
print(is_float(s2))


# ------------------------------------ РЕШЕНИЕ ЧЕРЕЗ ИСКЛЮЧЕНИЯ -------------------------------------------------
from ast import literal_eval # используем если не 'is_int' и не 'is_float'


def is_int(s):
    '''Функция проверяет, можно ли данные в строке без ошибок преобразовать тип данных int'''
    try:
        res = int(s)
        return type(res)
    except Exception:
        return "Введенные данные не 'int'."

def is_float(s):
    '''Функция проверяет, можно ли данные в строке без ошибок преобразовать тип данных float'''
    try:
        res = float(s)
        return type(res)
    except Exception:
        return "Введенные данные не float"


def main():
    '''Функция проверяет какого типа данные, введеннные пользователем'''
    running = True
    while running:
        try:
            escape = input("Продолжить программу y/n: ")
            if escape == "y":
                input_data = input("Введите данные: ")
                if is_int(input_data) is int:
                    print(is_int(input_data))
                elif is_float(input_data) is float:
                    print(is_float(input_data))
                else:
                    print(type(literal_eval(input_data)))
            elif escape == "n":
                print("Выход из программы.")
                running = False
            else:
                print("Некорректный ввод. Введите y/n")
        except (ValueError, SyntaxError):
            # строка, поэтому возвращаем тип данных str
            print(str)


# run
if __name__ == "__main__":
    main()
