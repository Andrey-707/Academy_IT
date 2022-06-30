# Sudoku.tkinter 9.Генератор уровней.Корректность значений в ячейке.

import os, random

from tkinter import *
from tkinter import ttk, font
from Create_sudoku import create_sudoku


def prep_cells():
    """
    Функция добавляет ячейки на игровое поле.
    """
    global cells
    for rows in range(row_count):
        row = []
        for columns in range(col_count):
            x_beg = columns*cell_size
            x_end = x_beg + cell_size
            y_beg = rows*cell_size
            y_end = y_beg + cell_size
            rect = canv.create_rectangle(x_beg, y_beg, x_end, y_end, width=1, fill=colors[2])
            row.append([0, rect])
        cells.append(row)

def draw_lines():
    """
    Функция добавляет разделительные линии для ячеек.
    """
    canv.create_line(3, 0, 3, canv_height, width=3, fill=colors[0])
    for i in range(1, 4):
        x = cell_size*3*i
        canv.create_line(x, 0, x, canv_height, width=3, fill=colors[0])

    canv.create_line(0, 3, canv_width, 3, width=3, fill=colors[0])
    for i in range(1, 4):
        y = cell_size*3*i
        canv.create_line(0, y, canv_width, y, width=3, fill=colors[0])

def prep_digitcells():
    """
    Функция добавляет справа поле цифр.
    """
    x_beg = 0
    x_end = cell_size
    for i in range(row_count+1):
        y_beg = cell_size*i
        y_end = y_beg + cell_size
        rect = canv_right.create_rectangle(x_beg, y_beg, x_end, y_end, width=3, fill=colors[2], tag='dig' + str(i))
        if i > 0:
            loc_text = str(i)
            canv_right.create_text(x_beg+1+cell_size/2, y_beg+1+cell_size/2, width=3, text=loc_text,
                fill=colors[0], font=dig_font)
    canv_right.create_line(2, 0, 2, canv_height + cell_size, width=3, fill=colors[0])
    canv_right.create_line(0, 2, cell_size, 2, width=3, fill=colors[0])

def fnc_load():
    """
    Функция загружает пазл на игровое поле.
    """
    lvl_num = correct_lvl()
    var_lvl.set(lvl_num)
    read_cells(lvl_num)

def read_cells(lvl_num):
    """
    Функция считывает данные из файла.
    """
    syms = 90 # количество символов в одном пазле
    delta = 9 # количество символов перевода строки в одном пазле
    f.seek((syms + delta)*(lvl_num - 1))
    lst_loc = [str(j) for i in list(f.read()) for j in i if j not in '\n']
    for i in range(cells_count):
        row_num = i//row_count
        col_num = i%row_count
        if lst_loc[i] not in '0.':
            val = lst_loc[i]
        else:
            val = ' '
        make_fragm(val, row_num, col_num)

def write_cells():
    """
    Функция записывает ячейку.
    """
    lst_loc = ['.' for num in range(cells_count)]
    for num in range(cells_count):
        row_num = num//row_count
        col_num = num%row_count
        number = cells[row_num][col_num][0]
        if number == '0':
            lst_loc[num] = '.'
        else:
            lst_loc[num] = number

    tmp_txt = ''.join(lst_loc).replace(' ', '.')
    data_txt = ''
    for i in range(9):
        data_txt = data_txt + tmp_txt[9*i:9*i+9] + '\n'
    f.write(data_txt)

def fnc_clear():
    """
    Функция очищает игровое поле от цифр.
    """
    for row in range(row_count):
        for col in range(col_count):
            make_fragm('0', row, col)

def fnc_save():
    """
    Функция записывает/перезаписывает уровень.
    """
    syms = 90 # количество символов в одном пазле
    delta = 9 # количество символов перевода строки в одном пазле
    lvl_num = correct_lvl()
    f.seek((syms + delta)*(lvl_num - 1))
    write_cells()
    f.seek(0, 2)

def correct_lvl():
    """
    Функция выбирает корректный уровень с защитой на границы.
    """
    lvl_num = var_lvl.get()
    if lvl_num < 1:
        lvl_num = lvl_count + 1 + lvl_num
        if lvl_num < 1:
            lvl_num = 1

    if lvl_num >= lvl_count:
        lvl_num = lvl_count

    var_lvl.set(lvl_num)
    return lvl_num

def fnc_add():
    """
    Функция добавляет уровнень в память программы.
    """
    global lvl_count
    f.seek(0, 2)
    write_cells()
    lvl_count = f.seek(0, 2)//cells_count
    var_count.set(lvl_count)
    var_lvl.set(lvl_count)

def make_fragm(val, row_num, col_num):
    """
    Функция создает или добавляет фрагмент.
    """
    global cells
    cells[row_num][col_num][0] = val
    text_tag = 't' + str(row_num*col_count + col_num)
    try:
        canv.delete(text_tag)
    except Exception as ex:
        print(repr(ex))

    if val == '.' or val == '0':
        cell_text = ' '
    else:
        cell_text = str(val)

    x_beg = col_num*cell_size + cell_size//2
    y_beg = row_num*cell_size + cell_size//2
    canv.create_text(x_beg, y_beg, text=cell_text, fill=colors[0], font=dig_font, tag=text_tag)

def dig_mouse_click(event):
    """
    Функция обрабатывает события клика левой кнопки мышки по правой цифровой панели.
    """
    global sel_digit
    canv_right.itemconfig('dig' + sel_digit, fill=colors[2])
    sel_digit = str(event.y//cell_size)
    canv_right.itemconfig('dig' + sel_digit, fill=colors[1])

def mouse_click(event):
    """
    Функция обрабатывает события клика левой кнопки мышки по игровому полю.
    """
    row_num = event.y//cell_size
    col_num = event.x//cell_size

    # проверка на корректность
    if sel_digit != '0':
        # проверка колонки
        for col in range(col_count):
            if sel_digit == cells[row_num][col][0]:
                return
        # проверка строки
        for row in range(row_count):
            if sel_digit == cells[row][col_num][0]:
                return
        # ячейка (3х3)
        row_beg = (row_num//3)*3
        row_end = row_beg + 3
        col_beg = (col_num//3)*3
        col_end = col_beg + 3
        # список, элементрами которого будут значения ячейки 3х3
        lst_loc = []
        for row in range(row_beg, row_end):
            for col in range(col_beg, col_end):
                lst_loc.append(cells[row][col][0])
        # проверка ячейки
        if sel_digit in lst_loc:
            return

    make_fragm(sel_digit, row_num, col_num)

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

def solve():
    """
    Функция решения судоку.
    Заполняет игровое поле решенной головоломкой.
    """
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == '.' or grid[y][x] == '0':
                for n in range(1, 10):
                    number = str(n)
                    if possible(grid, y, x, number):
                        grid[y][x] = number
                        solve()
                        grid[y][x] = '0'
                return
    fill(grid)

def fill(grid):
    """
    Функция заполняет поле значениями из сетки.
    """
    for i in range(row_count):
        for j in range(col_count):
            make_fragm(grid[i][j], i, j)

def choose_puzzle():
    """
    Функция выбирает случайный файл из списка.
    """
    path = "All_SUDOKU"
    some_list = []

    for adress, dirs, files in os.walk(path): # walk() - функция-генератор
        for file in files:
            if '.txt' in file:
                some_list.append(file)
    rand_puzzle = random.choice(some_list)
    print("Puzzle choosen:", rand_puzzle)
    return rand_puzzle

# Главное окно и его параметры
root = Tk()
root.title("Sudoku Game") # title (шапка) окна
root.geometry("500x500") # определение размеров окна
root.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание окна)

# Список используемых цветов в HEX формате ['black, 'blond', 'pink']
colors = ['#000000', '#faf0be', '#ffc0cb']

# картинка фона
canvas_font = PhotoImage(file='png\\Sakura.png') 
image_font = Label(root, image=canvas_font)
image_font.place(x=0, y=0)

# стили символов и цифр
sym_font = font.Font(family='helvetica', size=13)
dig_font = font.Font(family='helvetica', size=12)

# '.' - стилизация для ВСЕГО
stl = ttk.Style()
stl.configure('.', font=sym_font, background=colors[0], foreground=colors[1])

# ПЕРВЯ СТРОКА ФОРМЫ
# поле номера уровня
Nums = ttk.Label(root, text='Num:', background=colors[0], foreground=colors[1])
Nums.grid(row=1, column=0, padx=(25,0), pady=(5,0), sticky='W')

# поле ввода номера уровня
var_lvl = IntVar()
var_lvl.set(1)
edt_lvl = ttk.Entry(root, width=5, textvariable=var_lvl, justify=RIGHT, font=sym_font)
edt_lvl.grid(row=1, column=1, padx=(0,5), pady=(5,0), sticky='W')

# поле номера уровня
ttk.Label(root, text='Map:', background=colors[0], foreground=colors[1]).\
    grid(row=1, column=2, padx=(5,0), pady=(5,0), sticky='W')

# поле ввода номера уровня
var_count = IntVar()
var_count.set(1)
edt_count = ttk.Entry(root, width=5, textvariable=var_count, justify=RIGHT, font=sym_font)
edt_count.grid(row=1, column=3, padx=(0,0), pady=(5,0), sticky='W')

# ВТОРАЯ СТРОКА ФОРМЫ
cells = []
cell_size = 42
row_count = 9
col_count = 9
canv_width = cell_size*row_count
canv_height = cell_size*col_count

# рамка для основной канвы
pnl_canv = Frame(root)
pnl_canv.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky='S')

# основная канва
canv = Canvas(pnl_canv, width=canv_width, height=canv_height, background=colors[2])
canv.pack(side='top', padx=(0,0), pady=(0,0))

# ТРЕТЬЯ СТРОКА ФОРМЫ
btn_width = 5 # ширина кнопок

# кнопка загрузки уровня
btn_load = Button(root, text='Load', width=btn_width, command=fnc_load)
btn_load.config(background=colors[0], foreground=colors[1], font=sym_font, bd=2)
btn_load.grid(row=3, column=0, padx=(15,0), pady=5, sticky='W')

# кнопка очистки уровня
btn_solve = Button(root, text='Solve', width=btn_width, command=solve)
btn_solve.config(background=colors[0], foreground=colors[1], font=sym_font, bd=2)
btn_solve.grid(row=3, column=1, padx=(5,0), pady=5, sticky='W')

# кнопка очистки уровня
btn_clear = Button(root, text='Clear', width=btn_width, command=fnc_clear)
btn_clear.config(background=colors[0], foreground=colors[1], font=sym_font, bd=2)
btn_clear.grid(row=3, column=2, padx=(5,0), pady=5, sticky='W')

# кнопка записи уровня
btn_clear = Button(root, text='Save', width=btn_width, command=fnc_save)
btn_clear.config(background=colors[0], foreground=colors[1], font=sym_font, bd=2)
btn_clear.grid(row=3, column=3, padx=(5,0), pady=5, sticky='W')

# кнопка добавления уровня
btn_clear = Button(root, text='Add', width=btn_width, command=fnc_add)
btn_clear.config(background=colors[0], foreground=colors[1], font=sym_font, bd=2)
btn_clear.grid(row=3, column=4, padx=(5,0), pady=5, sticky='W')

# ЦИФРОВОЕ ПОЛЕ СПРАВА
# рамка для цифрового поля
pnl_right = Frame(root)
pnl_right.grid(row=1, column=5, rowspan=2, padx=10, pady=5, sticky='S')

# колонка цифр
num_height = canv_height + cell_size
canv_right = Canvas(pnl_right, width=cell_size, height=num_height, background=colors[2])
canv_right.pack()

# БИНДЫ КНОПОК
sel_digit = '0'
canv_digit = 0  
canv_right.bind('<1>', dig_mouse_click) # обработка клика левой кнопки мышки по правой панели
canv.bind('<1>', mouse_click) # обработка клика левой кнопки мышки по основному полю

# Создание уровней (разбивает главный файл на 95 файлов puzzle)
all_puzzles = 'ALL_SUDOKU\\ALL_SUDOKU.txt'
create_sudoku(all_puzzles)

# ВЫБОР ФАЙЛА
# Выбрать случайный уровень (puzzle)
file = choose_puzzle()
file_path = 'ALL_SUDOKU\\' + file
f = open(file_path, 'r+') # открыть файл с возможностью добавления информации

# СОЗДАНИЕ СЕТКИ.
# Сетка в виде двумерного массива.
puzzle = f.read()
digits = [c for c in puzzle if c in '1234567890.']
grid = [digits[9*i:9*i+9] for i in range(9)]

cells_count = row_count*col_count
lvl_count = f.seek(0, 2)//cells_count
var_count.set(lvl_count)

# Запуск конструктора
prep_cells() # отрисовка ячеек
draw_lines() # отрисовка разделительныйх линий
prep_digitcells() # отрисовка цифр на правой панели

# замыкание цикла
root.mainloop()

# закрытие файла
f.close()
