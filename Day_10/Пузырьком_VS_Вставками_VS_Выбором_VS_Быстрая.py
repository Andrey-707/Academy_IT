# TEST. <<bubble_sort> vs <<insert_sort>> vs <<selection_sort>> vs <<hoar_sort>>

import random, time

from rich import print


# <<Сортировка пузырьком>>
A = [random.randint(1, 100) for i in range(5000)]
# print("List:\n", *A)

print(f"Тестирование сортировок проводится на списках длиной {len(A)} символов.\n" \
    "Каждый сортируемый список является копией первого.\n")

B = A.copy()
C = A.copy()
D = A.copy()

def bubble_sort(A):
    '''Сортировка списка "А" методом ПУЗЫРЬКА'''
    N = len(A)
    for bypass in range(1, N):
        for i in range(0, N-bypass):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


start1 = time.time()
bubble_sort(A)
finish1 = time.time() - start1

print("СОРТИРОВКА ПУЗЫРЬКОМ.")
# print("nSorted_List:\n", *A)
print("Время:", finish1, "сек")
print("Размер массива:", A.__sizeof__(), "байт")
print()


# <<Сортировка вставками>>
# print("List:\n", *B)

def insert_sort(A):
    '''Сортировка списка "А" ВСТАВКАМИ'''
    N = len(A)
    for top in range(1, N):
        i = top
        while i > 0 and A[i-1] > A[i]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1


start2 = time.time()
insert_sort(B)
finish2 = time.time() - start2

print("СОРТИРОВКА_ВСТАВКАМИ.")
# print("nSorted_List:\n", *B)
print("Время:", finish2, "сек")
print("Размер массива:", B.__sizeof__(), "байт")
print()


# <<Сортировка выбором>>
# print("List:\n", *C)

def selection_sort(A):
    '''Сортировка списка "А" методом ВЫБОРА'''
    N = len(A)
    for pos in range(0, N-1):
        for i in range(pos+1, N):
            if A[i] < A[pos]:
                A[i], A[pos] = A[pos], A[i]


start3 = time.time()
selection_sort(C)
finish3 = time.time() - start3

print("СОРТИРОВКА ВЫБОРОМ.")
# print("nSorted_List:\n", *C)
print("Время:", finish3, "сек")
print("Размер массива:", C.__sizeof__(), "байт")
print()


# <<Сортировка Тони Хоара (быстрая сортировка)>>
#print("List:\n", *D)

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

start4 = time.time()
hoar_sort(D)
finish4 = time.time() - start4

print("БЫСТРАЯ СОРТИРОВКА.")
# print("nSorted_List:\n", *D)
print("Время:", finish4, "сек")
print("Размер массива:", D.__sizeof__(), "байт")
