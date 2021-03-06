# Задача№4.стр.31.Таблицы.
# Необходимо написать функцию, которая будет печатать таблицу с заглавными и строчными буквами в красивом формате
# Эта функция должна принимать в качестве аргумента список с буквами, которые необходимо поставить в таблицу.
# Если в списке одна буква, то таблица выглядит так:
# ------------------------------- # 31 -
# | A a |     |     |     |     | # 6 - | и 25 пробелов (если без символов) или 15 пробелов (если с символами)
# ------------------------------- # 31 -
# Если букв 14, то воттак:
# -------------------------------
# | A a | B b | C c | D d | E e | 
# -------------------------------
# | F f | G g | H h | I i | J j | 
# -------------------------------
# | K k | L l | M m | N n |     | 
# -------------------------------
# букв в списке может быть неограничено.

from rich import print


# символьная строка
# print("-" * 31)
# for _ in range(6):
#     print("|", "   ", end=" ")
# print()
# print("-" * 31)
"""
-------------------------------
|     |     |     |     |     |
-------------------------------
"""

# Таблица с ручным форматированием (границы вводятся вручную).
def table(s):
    '''Таблица размером в ширину 5 столбцов, один столбец содержит пару букв (.upper() и .lower())'''
    q = len(s) % 5 # величина, равная длине строки s, кратной 5
    # условие если q не кратно 5 ( не 5, не 10, не 15 и т.д.)
    if q != 0:
        s += " "*(5 - q) # s += " "*(5 - 3), т.к. длина строки 18 символов - добавить два пробела в конец таблицы
    print(s) # абвгдghyb csdbh wf - 18 символов

    # верхняя граница таблицы
    print("-" * 31)
    # основная часть таблицы
    for i in range(len(s)//5):
        print(f"| {s[0+i*5].upper()} {s[0+i*5].lower()} | {s[1+i*5].upper()} {s[1+i*5].lower()} "
              f"| {s[2+i*5].upper()} {s[2+i*5].lower()} | {s[3+i*5].upper()} {s[3+i*5].lower()} "
              f"| {s[4+i*5].upper()} {s[4+i*5].lower()} |")
    # нижняя граница таблицы
    print("-" * 31)


# run
table("абвгдghyb csdbh wf")

"""OUT:
-------------------------------
| А а | Б б | В в | Г г | Д д |
| G g | H h | Y y | B b |     |
| C c | S s | D d | B b | H h |
|     | W w | F f |     |     |
-------------------------------
"""


############################################ ЕЩЁ СИМВОЛЬНЫЕ ТАБЛИЦЫ ################################################
from prettytable import PrettyTable


# Определяем шапку и данные основной части таблицы.
th = ["абвгдghyb csdbh wf"] # шапка таблицы
td = ["A a", "B b", "C c", "D d", "E e"] # основная часть таблицы

# Подсчитаем кол-во столбцов на будущее. В итоге получаем 1 столбец
columns = len(th)

# Определяем таблицу
table = PrettyTable(th)

# Cкопируем список td, на случай если он будет использоваться в коде дальше.
td_data = td[:]

# Входим в цикл который заполняет нашу таблицу. Цикл будет выполняться до тех пор пока у нас не кончатся данные
# для заполнения строк таблицы (список td_data).
while td_data:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td_data[:columns])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td_data = td_data[columns:]

# Печатаем таблицу
print(table)

"""OUT:
+--------------------+
| абвгдghyb csdbh wf |
+--------------------+
|        A a         |
|        B b         |
|        C c         |
|        D d         |
|        E e         |
+--------------------+
"""

# -------------------------------- НАОБОРОТ --------------------------------------------------------------------
from prettytable import PrettyTable


# Определяем шапку и данные основной части таблицы.
th = ["A a", "B b", "C c", "D d", "E e"] # шапка таблицы
td = ["абвгдghyb", "csdbh", "wf", "csdbh", "wf"] # основной блок таблицы

# Подсчитаем кол-во столбцов на будущее. В итоге получаем 5 столбцов.
columns = len(th)

# Определяем таблицу.
table = PrettyTable(th)

# Cкопируем список td, на случай если он будет использоваться в коде дальше.
td_data = td[:]

# Входим в цикл который заполняет нашу таблицу. Цикл будет выполняться до тех пор пока у нас не кончатся данные
# для заполнения строк таблицы (список td_data).
while td_data:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td_data[:columns])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td_data = td_data[columns:]

# Печатаем таблицу
print(table)

"""OUT:
+-----------+-------+-----+-------+-----+
|    A a    |  B b  | C c |  D d  | E e |
+-----------+-------+-----+-------+-----+
| абвгдghyb | csdbh |  wf | csdbh |  wf |
+-----------+-------+-----+-------+-----+
"""