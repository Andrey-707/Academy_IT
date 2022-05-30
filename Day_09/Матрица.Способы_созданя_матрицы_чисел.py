from rich import print

################################## Создание матрицы через input() ###########################################

# так
m = int(input("Введите число столбцов матрицы: ")) # m - число столбцов (или вложенных списков)
matrix = []
for i in range(m):
    row = [int(x) for x in input().split()]
    matrix.append(row)

print(matrix)

# или так, используя 'list comprehension'
m = int(input("Введите число столбцов матрицы: ")) # m - число столбцов (или вложенных списков)
matrix = [[int(x) for x in input().split()] for i in range(m)]

print(matrix)


################################# Создание матрицы рандомных  ######################################################

N = 4 # количество строк (или вложенных списков)
M = 4  # количество столбцов

matrix = [[0]*M for i in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = random.randint(1, 10)

# или так, используя 'list comprehension'
matrix = [[random.randint(1, 10) for x in range(N)] for j in range(M)]


##################### Создание матрицы размерами n x m с заполнением элементами от 0 до len(n) ######################

# 'n' - количество строк (или вложенных списков) и 'm' - столбцов
matrix = []
n = int(input("x"))
m = int(input("y"))
r = 0

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(r)
        r += 1
print(matrix)


######################## Создание матрицы размерами n x m с заполнением элементами через input() ################

# 'n' - количество строк (или вложенных списков) и 'm' - столбцов
n, m = (int(i) for i in input("n & m:\n").split())
matrix = [[int(j) for j in input().split()] for i in range(n)]


################################## Форматный (построчный) вывод элементов матрицы #################################
for i in matrix:
    for j in i:
        print(f"{j:3d}", end="")
    print()