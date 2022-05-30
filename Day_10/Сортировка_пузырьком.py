# СОРТИРОВКА МЕТОДОМ ПУЗЫРЬКА

import random, time

from rich import print


def bubble_sort(A):
    '''Сортировка списка "А" методом ПУЗЫРЬКА'''
    N = len(A)
    for bypass in range(1, N):
        for i in range(0, N-bypass):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


A = [random.randint(1, 100) for i in range(1000)]
# print("List:\n", *A)

start = time.time()
bubble_sort(A)
finish = time.time() - start

print("СОРТИРОВКА ПУЗЫРЬКОМ.")
# print("nSorted_List:\n", *A)
print("\nВремя:", finish)
