# Сортировка Тони Хоара (БЫСТРАЯ СОРТИРОВКА).

import random, time

from rich import print


def hoar_sort(A):
    '''Сортировка Хоара'''
    if len(A) <= 1: # крайний случай
        return # <=> return None
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else: # x > barrier
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


A = [random.randint(1, 100) for i in range(100)]
print("List:\n", *A)

start = time.time()
hoar_sort(A)
finish = time.time() - start

print("БЫСТРАЯ СОРТИРОВКА.")
# print("nSorted_List:\n", *A)
print("\nВремя:", finish)
