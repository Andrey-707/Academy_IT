# СОРТИРОВКА ВСТАВКАМИ

import random, time

from rich import print


def insert_sort(A):
    '''Сортировка списка "А" ВСТАВКАМИ'''
    N = len(A)
    for top in range(1, N):
        i = top
        while i > 0 and A[i-1] > A[i]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1


A = [random.randint(1, 100) for i in range(1000)]
# print("List:\n", *A)

start = time.time()
insert_sort(A)
finish = time.time() - start

print("СОРТИРОВКА_ВСТАВКАМИ.")
# print("nSorted_List:\n", *A)
print("\nВремя:", finish)
