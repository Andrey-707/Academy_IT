# Решение головоломок. SUDOKU_1.
# Программа решает головоломку SUDOKU, которая передается в виде текстового файла, пустые ячайки
# имеют значение '.'

import pathlib, time

from rich import print


def read_sudoku(path):
    """
    Принимает путь (файл .txt), открывает файл на чтение.
    Возвращает данные из файла (сетку или список списков).
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    digits = [c for c in puzzle if c in '123456789.']
    grid = [digits[9*i: 9*i+9] for i in range(9)]
    return grid


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


def possible(grid, y, x, n):
    """
    Функция проверяет, может ли число находиться в определенной ячейке. Принимает сетку, 
    координаты числа и число. Возвращает логическое значение.
    """
    numbers = [str(i) for i in range(1, 10)]
    if n not in numbers:
        return False
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve(grid):
    """
    Функция решения судоку. Принимает сетку.
    Выводит на печать решенную головоломку.
    """
    for y in range(9):
        for x in range(9):
            if grid[y][x] == '.':
                for n in range(1, 10):
                    number = str(n)
                    if possible(grid, y, x, number):
                        grid[y][x] = number
                        solve(grid)
                        grid[y][x] = '.'
                return
    finish = time.time() - start
    print_grid(grid)
    print("Время:", round(finish, 3), "sec")


# run
grid = 'puzzle5.txt'
print(f"[yellow]Входные данные:\nРешаем {grid}[/]")
print_grid(read_sudoku(f'Base_SUDOKU\\{grid}'))

print(f"[yellow]Выходные данные:\nРешаем {grid}[/]")
start = time.time()
solve(read_sudoku(f'Base_SUDOKU\\{grid}'))
