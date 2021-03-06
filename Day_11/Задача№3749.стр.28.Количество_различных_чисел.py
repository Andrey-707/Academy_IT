# Задача№3749.стр.28.Количество различных чисел
# Дан список чисел, который может содержать до 100000 чисел. Определите, сколько в нем встречается различных чисел.

# Примечание. Эту задачу на Python можно решить в одну строчку.

# Входные данные:
# Вводится список целых чисел. Все числа списка находятся на одной строке.
# Выходные данные:
# Выведите ответ на задачу.

# Примеры
# Входные данные:
# 1 2 3 2 1
# Выходные данные:
# 3
# Входные данные:
# 1 2 3 4 5 6 7 8 9 10
# Выходные данные:
# 10

from rich import print


# ----------------------------------- Список от пользователя -------------------------------------------------------
some_nums = input("Введите числа через пробел:\n")
some_list = [int(i) for i in some_nums.split()] # list comprehension
# print(some_list) # для просмотра списка чисел раскомментировать

# Если список подходит по условию задачи
if len(some_list) <= 100000:
    result = len(set(some_list))
    nums = set(some_list)
    print(f"Различных чисел в списке: {result}.")
    print(*nums)
else:
    print("Допустимая длина списке 100000 чисел.")


# ------------------------------------- Список рандомных чисел ------------------------------------------------------
import random


# При помощи модуля 'random' создадим список, на входе получим границы рандомных чисел от 'a' до 'b' и длину списка 'n'
a = int(input("от: "))
b = int(input("до: "))
n = int(input("Длина списка: "))
rand_list = [random.randint(a, b) for i in range(n)]
print(*rand_list) # для просмотра списка чисел раскомментировать

# Если список подходит по условию задачи
if len(rand_list) <= 100000:
    result = len(set(rand_list))
    nums = set(rand_list)
    print(f"Различных чисел в списке: {result}.")
    print(*nums)
else:
    print("Допустимая длина списке 100000 чисел.")
