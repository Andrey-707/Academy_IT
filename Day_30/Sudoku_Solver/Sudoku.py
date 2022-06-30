# Решение головоломок. SUDOKU.

import pathlib

from rich import print


def read_sudoku(path):
    """
    Принимает путь (файл .txt), открывает файл на чтение.
    Возвращает данные из файла (сетку или список списков).
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
        # print(puzzle)
    digits = [c for c in puzzle if c in '123456789.']
    # print(digits)
    grid = [digits[9*i: 9*i+9] for i in range(9)]
    # print(grid)

    return grid

# print(read_sudoku('puzzle1.txt'))


def print_grid(grid):
    """
    Принимает сетку, выводит отформатированный вывод сетки на экран.
    """
    for i in range(9):
        if i % 3 == 0:
            if i == 0:
                print("┎──────────────────────────┒")
            else:
                print("┠─────────────────────────┨")
        for j in range(9):
            if j % 3 == 0:
                print("┃ ", end="")
            if j == 8:
                print(grid[i][j], end=" ┃ ")
            else:
                print(grid[i][j], end=" ")
        print()
    print("┖──────────────────────────┚")

# print_grid(grid=read_sudoku('puzzle1.txt'))


def get_row(grid, row_i):
    """
    Принмает сетку и номер строки, возвращает строку.
    """
    return [r for r in grid[row_i] if r in '123456789']

# print(get_row(grid=read_sudoku('puzzle1.txt'), row_i=0)) # для строки с индексом 0


def get_col(grid, col_i):
    """
    Принмает сетку и номер столбца, возвращает столбец.
    """
    return [c for c in [row[col_i] for row in grid] if c in '123456789']

# print(get_col(grid=read_sudoku('puzzle1.txt'), col_i=0)) # для столбца с индексом 0


def get_block(grid, row_i, col_i):
    """
    Принмает сетку, номер строки и номер столбца, возвращает блок.
    """
    if row_i % 3 == 1:
        row_i -= 1
    elif row_i % 3 == 2:
        row_i -= 2
    if col_i % 3 == 1:
        col_i -= 1
    elif col_i % 3 == 2:
        col_i -= 2
    return [c for c in grid[row_i][col_i:col_i+3] +
            grid[row_i+1][col_i:col_i+3] +
            grid[row_i+2][col_i:col_i+3] if c in '123456789']

# print(get_block(grid=read_sudoku('puzzle1.txt'), row_i=0, col_i=0)) # для строки и столбца с индексом 0


def grid_al(grid):
    """
    Принмает сетку, возвращает True, если судоку не решено и False, если решено.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] not in '123456789':
                return True
    return False


def one_1(grid):
    """
    Функция одного прохода цикла для решения судоку, принимает сетку, возвращает обновленную сетку.
    """
    for row_i in range(9):
        for col_i in range(9):
            # grid[i][j]
            if grid[row_i][col_i] == ".":
                row = get_row(grid, row_i)
                col = get_col(grid, col_i)
                block = get_block(grid, row_i, col_i)
                my_set = set(row + col + block)
                # print(my_set)
                if len(my_set) == 8:
                    zs_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - my_set
                    grid[row_i][col_i] = list(zs_set)[0]
    return grid


def one_2(grid):
    """
    Функция второго прохода цикла для решения судоку, принимает сетку, возвращает обновленную сетку.
    Она необходима, если после one_1 программа зацикливается и не выдвает однозначного решения.
     """
    for row_i in range(9):
        for col_i in range(9):
            # grid[i][j]
            if grid[row_i][col_i] == ".":
                row = get_row(grid, row_i)
                col = get_col(grid, col_i)
                block = get_block(grid, row_i, col_i)
                my_set = set(row + col + block)
                print(my_set)
                if len(my_set) == 7:
                    zs_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - my_set
                    zs_list = list(zs_set)
                    vibor = 0
                    grid[row_i][col_i] = zs_list[vibor]
                    return grid, zs_set, vibor


def copy_grid(grid):
    """
    Принмает сетку, копирует сетку, возвращает сетку как старую сетку.
    """
    old_grid = []
    for i in grid:
        old_grid.append(i.copy())

    return old_grid


def solve(grid):
    """
    Алгоритм решения судоку, принимает сетку.
    """
    print_grid(grid)
    # пока True (судоку не решено) цикл работает
    while grid_al(grid):
        old_grid = copy_grid(grid)
        grid = one_1(grid) # 1 проход цикла для решения судоку
        print_grid(grid)
        if old_grid == grid:
            print(old_grid)
            print(grid)
            grid, zs_set, vibor = one_2(grid)


solve(read_sudoku('puzzle3.txt'))
