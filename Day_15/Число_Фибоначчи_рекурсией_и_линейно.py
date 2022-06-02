# ЧИСЛО ФИБОНАЧЧИ.
from time import time
from rich import print


print("Program start")
################################################# TEST_1 ##############################################################
# Метод циклов.

def fib(n):
    f1 = f2 = 1
    # print(f1, end=' ')
    # print(f2, end=' ')

    for i in range(2, n):
        f1, f2 = f2, f1+f2 # сумма двух предыдущих чисел
        if i == n-1:
            return f2

# run TEST_1
start1 = time()
print("RESULT:", fib(45))                                                   # RESULT: 1134903170
print("TIME:", time() - start1)                                             # TIME: 0.0010001659393310547

print() # пустая строка

################################################# TEST_2 ##############################################################
# Метод циклов.

def fib(n):
    f1 = f2 = 1
    i = 0
    while i < n - 2:
        f1, f2 = f2, f1 + f2
        i += 1
    return f2

# run TEST_2
start2 = time()
print("RESULT:", fib(45))                                                   # RESULT: 1134903170
print("TIME:", time() - start2)                                             # TIME: 0.0009999275207519531

print() # пустая строка

################################################# TEST_3 ##############################################################
# Через импорт math.

import math

def fib(n):
    golden_ration = (1 + math.sqrt(5))/2
    val = (golden_ration**n - (1 - golden_ration)
        **n)/math.sqrt(5)
    return int(round(val))

# run TEST_3
start3 = time()
print("RESULT:", fib(45))                                                    # RESULT: 1134903170
print("TIME:", time() - start3)                                              # TIME: 0.002000093460083008

print() # пустая строка

################################################# TEST_4 ##############################################################
# Метод циклов.

def fib():
    f1, f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1 + f2

# run TEST_4
n = 45
start4 = time() 
for i, f in zip(range(n+1), fib()):
    if i == 45:
        # print("{i:3}: {f:3}".format(i=i, f=f))
        print("RESULT:", f)                                                  # RESULT: 1134903170
print("TIME:", time() - start4)                                              # TIME: 0.0009999275207519531

print() # пустая строка

################################################# TEST_4 ##############################################################
# Динамическое программирование.

def fib(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# run TEST_4
start4 = time()
print("RESULT:", fib(45))                                                    # ORESULT: 1134903170
print("TIME:", time() - start4)                                              # TIME:  0.0

print() # пустая строка

################################################# TEST_5 ##############################################################
# Рекурсия. В данной асимптотике число Fib растет экспоненциально. ТАКАЯ АСИМПТОТИКА НЕ ДОПУСТИМА!

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# run TEST_3
start5 = time()
print("RESULT:", fib(45))                                                    # RESULT: 1134903170
print("TIME:", time() - start5)                                              # TIME: 398.0466010570526

# Такая рекурентрая асимптотика вычисления числа Фибоначчи ОЧЕНЬ медленная, она равна O(Fibn)
# Время выполнения поиска числа Фибоначчи при n = 45 fib(45) равна ~ 398 СЕК

print() # пустая строка

################################################# TEST_6 ##############################################################
# Минимализация дерева Фибоначчи путем сохранения данных

# ускорение достигнуто путем сохранения ранее посчитанных данных (если посчитано fib(n-1), дальше функция его возвращает)
# Время выполнения поиска числа Фибоначчи при n = 45 fib(45) равна ~ 0.0 СЕК

from functools import lru_cache


@lru_cache()
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# run TEST_6
start6 = time()
print("RESULT:", fib(45))                                                    # RESULT: 1134903170
print("TIME:", time() - start6)                                              # TIME: 0.0010001659393310547

print("Program finish")