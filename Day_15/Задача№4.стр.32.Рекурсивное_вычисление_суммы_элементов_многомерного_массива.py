# Задача№4.стр.32.Рекурсивное вычисление суммы элементов многомерного массива
# Напишите функцию def find_max(L), которая будет выполняться рекурсивно и вычислять сумму чисел из списка (с поддержкой 
# вложенных списков).

# Пример.
# Ввод:
# list1 = [-3, 8, 4,-7, [-1, 8, [2, [-4, 3]]]]
# Вывод:
# 10

from rich import print


# !!! Для этой задачи в n-мерном массиве глубина рекурсии равна количеству n массивов rec_deep == n И
# rec_deep < 1000 !!!

def get_summ1(L:list):
    '''Рекурсивная функция вычисления суммы элементов многомерного массива'''
    global rec_deep
    rec_deep += 1

    summ = 0
    for i in L:
        # если элемент i списка является списком - вызывай функцию get_summ1(), параметром которой будет этот элемент i
        if type(i) == type([]):
            summ += get_summ1(i)
        # если элемент i списка не является списком - добавляй его к сумме
        else:
            summ += i
    return summ


# run
rec_deep = 0 # переменная-счетчик, считает глубину рекурсии
list1 = [-3, 8, 4,-7, [-1, 8, [2, [-4, 3]]]]
print("[bold magenta]IN:[/]")
print(list1)

print("[bold magenta]OUT:[/]")
print("сумма элементов:", get_summ1(list1))
print("глубина рекурсии:", rec_deep)

print() # пустая строка


############################################################################################################
# Ещё один вариант решения
def get_summ2(L:list, res=0):
    '''Рекурсивная функция вычисления суммы элементов многомерного массива'''
    if L == []:
        # print("-")
        return res
    elif type(L[0]) == list:
        # print("++", type(L[0]))
        res = get_summ2(L[0], res)
    elif type(L[0]) == int:
        # print("+++", type(L[0]))
        res += L[0]
        res = get_summ2(L[1:], res)
    return res


# run
list1 = [-3, 8, 4,-7, [-1, 8, [2, [-4, 3]]]]
print("[bold magenta]IN:[/]")
print(list1)

print("[bold magenta]OUT:[/]")
print("сумма элементов:", get_summ2(list1))
