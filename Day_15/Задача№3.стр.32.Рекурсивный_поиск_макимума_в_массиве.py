# Задача№3.стр.32.Рекурсивный поиск максимума в массиве.
# Напишите функцию def find_max(L), которая будет выполняться рекурсивно и определять максимальное число из списка.
# Ввод:
# list1 = [400, 1300, 700, 561, 123]
# Вывод:
# 1300

# Решение.
from rich import print


# поиск максимума (циклом)
# mx = 0 # значение, в которое будет записываться максимум
# for i in list1:
#     if i > mx:
#         mx = i
# print(mx)


# !!! Для этой задачи в одномерном массиве глубина рекурсии равна длине массива rec_deep == len(list1) И
# rec_deep < 1000 !!!


def find_max1(L:list):
    '''Рекурсивная функция поиска максимального значения в массиве'''
    global rec_deep
    rec_deep += 1

    if len(L) == 1:
        return L[0]
    else:
        x = find_max1(L[1:])
        return x if x > L[0] else L[0]


# run
rec_deep = 0 # переменная-счетчик, считает глубину рекурсии

# поиск максимума в списке A
list1 = [400, 1300, 700, 561, 123]
print("[bold magenta]IN:[/]")
print(list1)

print("[bold magenta]OUT:[/]")
print("максимум списка:", find_max1(list1))
print("глубина рекурсии:", rec_deep)

print() # пустая строка


################################################# RANDOM LIST ##############################################
import random


# run
rec_deep = 0 # переменная-счетчик, считает глубину рекурсии

# поиск максимума в списке A из 10 рандомных чисел
A = [random.randint(1, 100) for i in range(10)]
print("[bold magenta]IN:[/]")
print(A)

print("[bold magenta]OUT:[/]")
print("Максимум списка:", find_max1(A))
print("Глубина рекурсии:", rec_deep)

print() # пустая строка


##############################################################################################################
# Ещё один вариант решения
def find_max2(L:list, res=0):
    '''Рекурсивная функция поиска максимального значения в массиве'''
    global rec_deep
    
    if L == []:
        return res
    elif L[0] > res:
        res = L[0]
        res = find_max2(L[1:], res)
        rec_deep += 1
    else:
        res = find_max2(L[1:], res)
        rec_deep += 1
    return res


# run
rec_deep = 0 # переменная-счетчик, считает глубину рекурсии
# поиск максимума в списке A
list2 = [400, 1300, 700, 561, 123]
print("[bold magenta]IN:[/]")
print(list2)

print("[bold magenta]OUT:[/]")
print("Максимум списка:", find_max2(list2))
print("Глубина рекурсии:", rec_deep)
