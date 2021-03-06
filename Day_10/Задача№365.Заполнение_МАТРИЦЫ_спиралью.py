# Задача№365.Заполнение матрицы спиралью.
# Дано число n. Создайте массив A[2*n+1][2*n+1] и заполните его по спирали, начиная с числа
# 0 в центре клетки A[n+1][n+1]. Спираль выходит вверх, далее закручивается против часовой стрелки.

# Входные данные:
# программа получает на входе одно число n
# Выходные данные:
# программа должна вывести полученный массив, отводя на вывод каждого числа ровно три символа

# Пример:
# Входные данные:
# n = 2
# Выходные данные:
'''
12 11 10  9 24
13  2  1  8 23
14  3  0  7 22
15  4  5  6 21
16 17 18 19 20
'''
# ----------------------------------ПЕРВОЕ_РЕШЕНИЕ-------------------------------------------------------------------
# Заполнение матрицы шагами из центра по спирали против часовой стрелки.
from rich import print


n = int(input("n = "))  
N = 2*n + 1

matrix = [[0 for i in range(N)] for j in range(N)]
print(matrix, sep="\n", end="")

num = 1 # символ заполнения матрицы (с каждым шагом символ увеличивается на 1)

step = 2 # шаг вокруг центра (после прохождения каждого круга увеличивается на 2)

# заполнение матрицы против часовой стрелки
for i in range(N//2):
    # движение влево
    for j in range(step):
        matrix[-i + N//2 - 1][-j + i + N//2] = num
        num += 1
    # движение вниз
    for j in range(step):
        matrix[j - i + N//2][-i + N//2 - 1] = num
        num += 1
    # движение вправо
    for j in range(step):
        matrix[i + N//2 + 1][j - i + N//2] = num
        num += 1
    # движение вверх
    for j in range(step):
        matrix[-j + i + N//2][i + N//2 + 1] = num
        num += 1
    step += 2

# форматный (построчный) вывод элементов матрицы
print("-" * (n*2 + n//2)  + "Matrix" + "-" * (n*2 + n//2))
for i in matrix:
    for j in i:
        print(f"{j:3d}", end="")
    print()


# ----------------------------------ВТОРОЕ_РЕШЕНИЕ-------------------------------------------------------------------
# Аналогичное предыдущему, но обход выполняется иначе.
from rich import print


n = int(input("n = ")) 
N = 2*n + 1

matrix = [[0 for x in range(N)] for i in range(N)]
print(matrix, sep="\n", end="")

num = 1 # символ заполнения матрицы (с каждым шагом символ увеличивается на 1)

for rc in range(1, n + 1):  # rc - счетчик кругов
    i = n - rc
    for j in range(n + rc - 1, n - rc - 1, -1):
        matrix[i][j] = num
        num += 1
    for i in range(n - rc + 1, n + rc + 1):
        matrix[i][j] = num
        num += 1
    for j in range(n - rc + 1, n + rc + 1):
        matrix[i][j] = num
        num += 1
    for i in range(n + rc - 1, n - rc - 1, -1):
        matrix[i][j] = num
        num += 1

# форматный (построчный) вывод элементов матрицы
print("-" * (n*2 + n//2)  + "Matrix" + "-" * (n*2 + n//2))
for line in matrix:
    for number in line:
        print(f"{number:3d}", end="")
    print()


# ----------------------------------ТРЕТЬЕ_РЕШЕНИЕ-------------------------------------------------------------------
# Создание матрицы вынесено в функцию.
from rich import print


def spiral_matrix(n):
    '''Функция генерирует матрицу, заполненную символами, начиная с нуля. С каждым шагом символ
    заполнения увеличивается на единицу.
    Заполнение начинается из центра и продолжается против часовой стрелки'''
    N = 2*n + 1
    matrix = [[0]*N for i in range(N)] # генерация матрицы
    iterr = N * N # лимит итераций
    i = N//2-1 # инициализация точки запуска
    j = N//2 # инициализация точки запуска
    num = 1 # символ заполнения матрицы (с каждым шагом символ увеличивается на 1)
    while num < iterr:
        matrix[i][j] = num
        # Старт из центра (точка 1:2) влево
        # далее если мы на верхней стороне прямоугольника и не достигли левой стороны, то двигаемся влево: j-=1
        if i < j and i + j < N - 1:
            j -= 1
        # Из точки 1:1 двигаемся вниз
        # далее если мы на левой стороне прямоугольника и не достигли нижней стороны, то двигаемся вниз: i+=1
        elif i >= j and i + j <= N - 2:
            i += 1
        # Из точки 3:1 двигаемся вправо 
        # далее если мы на нижней сторона прямоугольника и мы не достигла правой стороны, то двигаемся вправо: j+=1
        elif i >= j + 1 and i + j > N - 2:
            j += 1
        # Иначе двигаемся вверх: i-=1
        else:
            i -= 1
        num += 1

    # форматный (построчный) вывод элементов матрицы
    print("-" * (n*2 + n//2)  + "Matrix" + "-" * (n*2 + n//2))
    for i in matrix:
        for j in i:
            print(f"{j:3d}", end="")
        print()


# run
if __name__ == "__main__":
    n = int(input("n = "))
    spiral_matrix(n)
