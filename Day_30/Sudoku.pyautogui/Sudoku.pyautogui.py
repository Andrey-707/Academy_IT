# Решение головоломок. SUDOKU. pyautogui
# Программа решает головоломку SUDOKU, которая передается в виде текстового файла либо через input()
# от пользователя, затем заполняет головоломку, выведенную на экран (на сайте или в окне приложения).

import pyautogui, pathlib, time

from rich import print


def read_sudoku(path):
    """
    Принимает путь (файл .txt), открывает файл на чтение.
    Возвращает данные из файла (сетку или список списков).
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    digits = [int(c) for c in puzzle if c in '1234567890']
    grid = [digits[9*i: 9*i+9] for i in range(9)]
    return grid


def print_grid(A):
    """
    Принимает сетку SUDOKU, выводит отформатировнную сетку на экран.
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
                print(A[i][j], end=" ┃ ")
            else:
                print(A[i][j], end=" ")
        print()
    print("┖──────────────────────────┚")


def possible(grid, y, x, n):
    """
    Функция проверяет, может ли число находиться в определенной ячейке SUDOKU.
    Принимает сетку, координаты числа и число. Возвращает логическое значение.
    """
    numbers = [i for i in range(1, 10)]
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


def make_grid():
    """
    Функция заполняет сетку SUDOKU данными, полученными от пользвателя (через input()).
    Возвращает заполненную сетку в виде двумерного массива 9 х 9.
    """
    A = []
    while True:
        row = list(input('Row '+ str(len(A)+1) + ': '))
        inst = [int(n) for n in row]
        A.append(inst)
        print('Row ' + str(len(A)) + ' compleate.')
        if len(A) == 9:
            break
    return A


def fill_grid(grid):
    """
    Функция заполняет головоломку SUDOKU данными при помощи инструментов библиотеки pyautogui.
    """
    final = [str(num) for row in grid for num in row]
    tmp = []
    for num in final:
        pyautogui.press(num)
        pyautogui.hotkey('right')
        tmp.append(num)
        if len(tmp) % 9 == 0:
            pyautogui.hotkey('down')
            for i in range(8):
                pyautogui.hotkey('left')


def solve():
    """
    Функция решения SUDOKU.
    """
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_grid(grid)
    time.sleep(3)
    fill_grid(grid)


# run
if __name__ == '__main__':
    print(f"[yellow]Входные данные:[/]")
    # grid = make_grid() # ручное заполнение сетки
    grid = read_sudoku('Test_pyautogui.txt') # заполнение сетки из файла
    print_grid(grid)
    print(f"[yellow]Выходные данные:[/]")
    solve()
