# Матрица. Максимум столбца и минимум строки.
import random

from rich import print


# создадим матрицу 3 х 3
'''
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
'''
n, m = (int(i) for i in input("Через пробел введите число строк и столбцов матрица:\n").split())
# matrix = [[int(i) for i in input().split()] for j in range(n)] # ввод элементов через input()
matrix = [[random.randint(1, 10) for i in range(n)] for j in range(n)] # рандомная матрица

# форматный (построчный) вывод элементов матрицы
for i in matrix:
    for j in i:
        print(f"{j:3d}", end="")
    print()

# поиск макимума в матрице
max_num = max([max(i) for i in matrix])
print("max_num", max_num)

# поиск минимума в матрице
min_num = min([min(i) for i in matrix])
print("min_num", min_num)

# вывод в строчку чисел столбца, в котором содержится максимальное значение матрицы
print("Column with max_num:")
for j in range(m):
    column = [line[j] for line in matrix]
    if max_num in column:
        print(*column)

# вывод в строчку чисел строки, в которой содержится минимальное значение матрицы
print("Row with min_num:")
for i in range(n):
    if min_num in matrix[i]:
        print(*matrix[i])
