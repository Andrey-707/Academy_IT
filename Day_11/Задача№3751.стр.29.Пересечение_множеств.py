# Задача№3751.стр.29.Пересечение множеств.
# Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа, которые входят как в 
# первый, так и во второй список в порядке возрастания.

# Примечание. и даже эту задачу на Python можно решить в одну строчку.

# Входные данные:
# Вводятся два списка чисел. Все числа каждого списка находятся на отдельной строке.
# Выходные данные:
# Выведите ответ на задачу.

# Пример
# Входные данные:
# 1 3 2
# 4 3 2
# Выходные данные:
# 2 3

from rich import print


# ----------------------------------- Список от пользователя --------------------------------------------------
some_nums1 = input("Введите числа через пробел:\n")
some_list1 = [int(i) for i in some_nums1.split()] # list comprehension
# print(*some_list1) # для просмотра списка чисел раскомментировать
set1 = set(some_list1)

some_nums2 = input("Введите числа через пробел:\n")
some_list2 = [int(i) for i in some_nums2.split()]
# print(*some_list2) # для просмотра списка чисел раскомментировать
set2 = set(some_list2)

# РЕШЕНИЕ:
# Если списки подходят по условию задачи
if len(some_list1) <= 10000 and len(some_list2) <= 10000:
    # пересечение множеств set.intersection(other_set) или set & other_set
    result = sorted(set1.intersection(set2))
    if len(result) != 0:
        print(f"Числа, которые входят в оба списка:\n{result}")
    else:
        print("Списки не имеют одинаковых чисел.")
else:
    print("Допустимая длина списке 10000 чисел.")

# ----------------------------------- Список рандомных чисел -------------------------------------------------
import random


# При помощи модуля 'random' создадим список, на входе получим границы рандомных чисел от 'a' до 'b' и длину списка 'n'
a = int(input("от: ")) # 1
b = int(input("до: ")) # 100
n = int(input("Длина списка: ")) # 10
rand_list1 = [random.randint(a, b) for i in range(n)]
print(*rand_list1)
set1 = set(rand_list1)

# При помощи модуля 'random' создадим список, на входе получим границы рандомных чисел от 'c' до 'd' и длину списка 'm'
c = int(input("от: ")) # 1
d = int(input("до: ")) # 100
m = int(input("Длина списка: ")) # 10
rand_list2 = [random.randint(c, d) for i in range(m)]
print(*rand_list2)
set2 = set(rand_list2)

# РЕШЕНИЕ:
# Если списки подходят по условию задачи
if len(rand_list1) <= 10000 and len(rand_list2) <= 10000:
    # пересечение множеств set.intersection(other_set) или set & other_set
    result = sorted(set1.intersection(set2))
    if len(result) != 0:
        print("Числа, которые входят в оба списка:")
        print(*result)
    else:
        print("Списки не имеют одинаковых чисел.")
else:
    print("Допустимая длина списке 10 000 чисел")
