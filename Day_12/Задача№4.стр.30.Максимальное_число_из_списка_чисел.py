# Задача№4.стр.30.Максимальное число из списка чисел.
# У вас есть список чисел, напишите функцию, которая составляет из этих чисел максимальное число.
# Например: [61, 228, 9] -> 961228

from rich import print


def f(n:int):
    '''Рекурсивная функция вычисления факториала числа'''
    assert n >= 0, "Факториал отрицательного не определен."
    if n == 0:
        return 1
    return f(n-1)*n


def max_A(A:list):
    '''Функция расчитана на карту переборов, по средствам карты перебирает все возможные
    варианты и выбирает max'''
    max_num = 0
    for i in bust_map:
        ch = int(str(A[i[0]]) + str(A[i[1]]) + str(A[i[2]]))
        # print(ch) # выводит все возможные комбинации
        # выбор максимального числа из шести
        if ch > max_num:
            max_num = ch

    return max_num


# Список чисел
A = [61, 911, 91]

# размер карты переборов равен факториалу длины списка, т.е. факториалу len(A)
# вычисляем размер карты переборов
print(f(len(A))) # OUT: 6

# составляем карту переборов размером 6
bust_map = [[0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0]]

# находим максимально число
print("Максимальное число:", max_A(A)) # OUT: Максимальное число: 9191161


######################################################################################################################

# РЕШЕНИЕ, ПРИ КОТОРОМ НУЖНО СГЕНЕРИРОВАТЬ МАКСИМАЛЬНУЮ ЦИФРУ ИЗ СПИСКА ЧИСЕЛ.
# т.е. если число состоит из трех цифр (951), оно может быть разбито на три составляющие - 9, 5 и 1

def max_number(A:list):
    '''Функция принимает на входе список, составляет из этого списка максимальное число.
    Возвращает данные в виде строки'''
    x = "".join(sorted([str(j) for i in A for j in str(i)], reverse=True))
    
    return x

# два простых примера
A = [61, 228, 9]
print(max_number(A)) # OUT: 986221
A = [61, 911, 91]
print(max_number(A)) # OUT: 9961111

# пример для списка с использованием рандома
import random

# список из трех элементов рандомных чисел от 1 до 99
A = [random.randint(1, 99) for i in range(3)]
print(f"IN:\n{A}")

# результат
print(f"OUT:\n{max_number(A)}") 
