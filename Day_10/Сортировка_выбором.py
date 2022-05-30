# СОРТИРОВКА МЕТОДОМ ВЫБОРА

import random, time

from rich import print


def selection_sort(A):
    '''Сортировка списка "А" методом ВЫБОРА'''
    N = len(A)
    for pos in range(0, N-1):
        for i in range(pos+1, N):
            if A[i] < A[pos]:
                A[i], A[pos] = A[pos], A[i]


A = [random.randint(1, 100) for i in range(100)]
print("List:\n", *A)

start = time.time()
selection_sort(A)
finish = time.time() - start

print("СОРТИРОВКА ВЫБОРОМ.")
# print("nSorted_List:\n", *A)
print("\nВремя:", finish)
