# Задача№3750.Количество совпадающих.
# Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте сколько чисел содержится
# одновременно как в первом списке, так и во втором.

# Примечание. Эту задачу на Python можно решить в одну строчку.

# Входные данные:
# Вводятся два списка чисел. Все числа каждого списка находятся на отдельной строке.
# Выходные данные:
# Выведите ответ на задачу.

# Пример
# Входные данные:
# 1 3 2
# 4 3 2
# Выходные данные:
# 2

# Решение задачи - это реализация алгоритма пересечения двух множеств.

import random

from rich import print


# создадим два списка рандомайзером, на входе получим возможные границы рандомных чисел и длину списка
a = int(input("от: ")) # 1
b = int(input("до: ")) # 100
n = int(input("Длина списка: ")) # 10

# Создание выборки рандомной числовой последовательности. При это n не может быть больше b
# some_list1 = list(random.sample(range(a, b), n))

# Первый список с рандомных чисел от a до b длиной n
some_list1 = [random.randint(a, b) for i in range(n)]
print("some_list1:", *some_list1)

print() # пустая строка

c = int(input("от: ")) # 1
d = int(input("до: ")) # 100
m = int(input("Длина списка: ")) # 10

# Создание выборки рандомной числовой последовательности. При это m не может быть больше c
# some_list2 = list(random.sample(range(c, d+1), m))

# Второй список с рандомных чисел от c до d длиной m
some_list2 = [random.randint(c, d) for i in range(m)]
print("some_list2:", *some_list2)

print() # пустая строка

# РЕШЕНИЕ:
# если списки по длине подходят по условию задачи
if len(some_list1) < 100000 and len(some_list2) < 100000:
    # пересечение множеств set.intersection(other_set) или set & other_set
    print("Найдено повторений в двух списках:", len(list(set(some_list1).intersection(set(some_list2)))))
    print("Эти числа:", *sorted(set(some_list1).intersection(set(some_list2))))
else:
    print("Списки могут содержать до 100000 чисел каждый")


# Числа можно вывести так же циклом. Чтобы убрать повторы используется свойство множества.
for i in set(some_list1):
    if i in set(some_list2):
        print(i, end=" ")
