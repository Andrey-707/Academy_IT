
import random

from rich import print


# создадим матрицу и выведем элементы этой матрицы на экран

def build_matrix(n, m):
    '''Функция создает матрицу n строк m столбцов'''
    matrix = []
    for i in range(n):
        internal_arr = []
        for j in range(m):
            #internal_arr.append(0) # либо заполнение нулями
            internal_arr.append(random.randint(1, 10)) # либо заполнение рандомными числами
        matrix.append(internal_arr)
    return matrix

def print_matrix(matrix):
    '''Функция выводит элементы матрицы на экан'''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:3d}", end="")
        print()

matrix_4x4 = build_matrix(4, 4)
print("--Матрица--")
print_matrix(matrix_4x4)

# посчитаем суммы строк и столбцов матрицы 
print("\nПосчитаем суммы строк и столбцов матрицы")
print("\n--Матрица--")
print_matrix(matrix_4x4)
for i in range(4): # длина строки матрицы matrix_4x4
    s = 0
    for j in range(4):
        s += matrix_4x4[i][j]
    print("Сумма строки", i+1, "равна", s)

print("\n--Матрица--")
print_matrix(matrix_4x4)
for j in range(4): # длина столбца матрицы matrix_4x4
    s = 0
    for i in range(4):
        s += matrix_4x4[i][j]
    print("Сумма столбца", j+1, "равна", s)

# обмен значениями между строками матрицы
def swap(arr, i, j):
    '''Функция перестановки элементов матрицы, где i и j - индексы строк матрицы'''
    arr[i], arr[j] = arr[j], arr[i]

# отобразим зеркально созданную матрицу
def mirror_reflection(matrix):
    '''Функция зеркального отображения строк матрицы'''
    for arr in matrix:
        for i in range(len(arr) // 2):
            swap(arr, i, len(arr) -1 - i)

mirror_reflection(matrix_4x4)
print("\nОтобразим зеркально матрицу")
print("--Матрица--")
print_matrix(matrix_4x4)

# отзеркалим матрицу обратно
mirror_reflection(matrix_4x4)

# заполним матрицу (диагональ левый верх в правый низ)
def replace_items(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = 2
            else: # i > j
                matrix[i][j] = 3

print("\nЗамена элементов матрицы")
print("--Матрица--")
replace_items(matrix_4x4)
print_matrix(matrix_4x4)

# заполним матрицу (обратная диагональ правый верх в левый низ)
def replace_items(matrix):
    for i in range(len(matrix)):
        n = len(matrix)
        for j in range(len(matrix[i])):
            if j == n-1 - i:
                matrix[i][j] = 1
            elif j > n-1 - i:
                matrix[i][j] = 2
            else: # j < n-1 - i
                matrix[i][j] = 3

print("\nЗамена элементов матрицы")
print("--Матрица--")
replace_items(matrix_4x4)
print_matrix(matrix_4x4)

print("\nОбход по строкам матрицы")
print("--Матрица--")
#print_matrix(matrix_4x4)
for i in range(4): # длина строки матрицы matrix_4x4
    for j in range(4):
        print(f"{matrix_4x4[i][j]:3d}", end="")
    print()

print("\nОбход по столбцам матрицы")
print("--Матрица--")
#print_matrix(matrix_4x4)
for j in range(4): # длина столбца матрицы matrix_4x4
    for i in range(4):
        print(f"{matrix_4x4[i][j]:3d}", end="")
    print()

print("\nОбратный обход по строкам матрицы")
print("--Матрица--")
#print_matrix(matrix_4x4)
for i in range(3, -1, -1): # длина строки матрицы matrix_4x4
    for j in range(3, -1, -1):
        print(f"{matrix_4x4[i][j]:3d}", end="")
    print()

print("\nnОбратный обход по столбцам матрицы")
print("\n--Матрица--")
#print_matrix(matrix_4x4)
for j in range(3, -1, -1): # длина столбца матрицы matrix_4x4
    for i in range(3, -1, -1):
        print(f"{matrix_4x4[i][j]:3d}", end="")
    print()

# матрица в одну строчку
n = 4
# 1  0  0  0
# 2  1  0  0
# 2  2  1  0
# 2  2  2  1
# размерность массива - это длина строки (передать число 4)
A = [[2] * i + [1] + [0] * (int(input("Размерность массива")) - i - 1) for i in range(n)]
# и форматный вывод
for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"{A[i][j]:3d}", end="")
    print()