# Sudoku.tkinter 06.Обработка событий загрузка игрового поля.

from tkinter import *
from tkinter import ttk
from tkinter import font


def prep_cells():
    """
    Функция добавляет ячейки.
    """
    global cells
    for rows in range(row_count):
        row = []
        for columns in range(col_count):
            x_beg = columns*cell_size
            x_end = x_beg + cell_size
            y_beg = rows*cell_size
            y_end = y_beg + cell_size
            rect = canv.create_rectangle(x_beg, y_beg, x_end, y_end, fill=canv_color)
            row.append([0, rect])
        cells.append(row)

def draw_lines():
    """
    Функция добавляет разделительные линии для ячеек.
    """
    canv.create_line(3, 0, 3, canv_height, width=3, fill='black')
    for i in range(1, 4):
        x = cell_size*3*i
        canv.create_line(x, 0, x, canv_height, width=3, fill='black')

    canv.create_line(0, 3, canv_width, 3, width=3, fill='black')
    for i in range(1, 4):
        y = cell_size*3*i
        canv.create_line(0, y, canv_width, y, width=3, fill='black')

def prep_digitcells():
    """
    Функция добавляет поле цифр.
    """
    x_beg = 0
    x_end = cell_size
    for i in range(row_count+1):
        y_beg = cell_size*i
        y_end = y_beg + cell_size
        rect = canv_right.create_rectangle(x_beg, y_beg, x_end, y_end, fill=canv_color,
            tag='dig' + str(i))
        if i > 0:
            loc_text = str(i)
            canv_right.create_text(x_beg+1+cell_size/2, y_beg+1+cell_size/2, text=loc_text,
                fill='black', font=dig_font)
    canv_right.create_line(2, 0, 2, canv_height + cell_size, fill='black')
    canv_right.create_line(0, 2, cell_size, 2, fill='black')

def fnc_load():
    """
    Создает игровое поле.
    """
    level_num = var_lvl.get()
    if level_num < 1:
        level_num = level_count + 1 + level_num
        if level_num < 1:
            level_num = 1
    
    if level_num >= level_count:
        level_num = level_count

    var_lvl.set(level_num)
    
    read_cells(level_num)

def read_cells(level_num):
    """
    Прочитать значения из файла.
    """
    f.seek(cells_count*(level_num - 1))
    lst_loc = [str(j) for i in list(f.read()) for j in i if j not in '\n']
    for i in range(cells_count):
        row_num = i//row_count
        col_num = i%row_count
        if lst_loc[i] not in '0.':
            val = lst_loc[i]
        else:
            val = ' '
        make_fragm(val, row_num, col_num) 

def fnc_clear():
    """
    Очищает игровое поле.
    """
    for i in range(row_count):
        for j in range(col_count):
            make_fragm(0, i, j)

def dig_mouse_click(event):
    """
    Обработчик событий клика левой кнопки мышки по правой цифровой панели.
    """
    global sel_digit
    canv_right.itemconfig('dig' + str(sel_digit), fill=canv_color)
    sel_digit = event.y//cell_size
    canv_right.itemconfig('dig' + str(sel_digit), fill=sel_color)

def mouse_click(event):
    """
    Обработчик событий клика левой кнопки мышки по основному полю.
    """
    row_num = event.y//cell_size
    col_num = event.x//cell_size
    make_fragm(sel_digit, row_num, col_num)

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

    x_beg = col_num*cell_size + cell_size//2
    y_beg = row_num*cell_size + cell_size//2
    if val == 0:
        cell_text = ' '
    else:
        cell_text = str(val)

    canv.create_text(x_beg, y_beg, text=cell_text, fill='black', font=dig_font, tag=text_tag)


# определение главного окна
root = Tk()
root.title("Sudoku Game") # title (шапка) окна
root.geometry("500x500") # определение размеров окна
root.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание окна)
root_color = 'black' # цвет поля
root.configure(background=root_color)

stl = ttk.Style()
sym_font = font.Font(family='helvetica', size=13)
dig_font = font.Font(family='helvetica', size=12)
stl.configure('.', font=sym_font, background=root_color, foreground='black')

# вторая строка формы
pnl_canv = Frame(root)
pnl_canv.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky='S')

cells = []

cell_size = 40

row_count = 9
col_count = 9

canv_width = cell_size*row_count
canv_height = cell_size*col_count
canv_color = 'skyblue'
canv = Canvas(pnl_canv, width=canv_width, height=canv_height, background=canv_color)
canv.pack(side='top', padx=(5,5), pady=(5,5))

prep_cells() # отрисовка ячеек
draw_lines() # отрисовка разделительныйх линий

# поле для номера уровня
Nums = ttk.Label(root, text='Num:', background='black', foreground='white')
Nums.grid(row=1, column=0, padx=(35,0), pady=(5,0), sticky='W')

# поле ввода номера уровня
var_lvl = IntVar()
var_lvl.set(1)
edt_lvl = ttk.Entry(root, width=5, textvariable=var_lvl, justify=RIGHT, font=sym_font)
edt_lvl.grid(row=1, column=0, padx=(100,0), pady=(5,0), sticky='W')

# поле для номера уровня
ttk.Label(root, text='Count:', background='black', foreground='white').\
    grid(row=1, column=1, padx=(20,0), pady=(5,0), sticky='W')

# поле ввода номера уровня
var_count = IntVar()
var_count.set(1)
edt_count = ttk.Entry(root, width=5, textvariable=var_count, justify=RIGHT, font=sym_font)
edt_count.grid(row=1, column=1, padx=(100,0), pady=(5,0), sticky='W')

btn_width = 8

# кнопка загрузки уровня
btn_load = Button(root, text='Load', width=btn_width, command=fnc_load)
btn_load.config(background='black', foreground='white', font=sym_font, bd=2)
btn_load.grid(row=3, column=0, padx=(15,0), pady=5, sticky='W')

# кнопка очистки уровня
btn_clear = Button(root, text='Clear', width=btn_width, command=fnc_clear)
btn_clear.config(background='black', foreground='white', font=sym_font, bd=2)
btn_clear.grid(row=3, column=1, padx=(100,5), pady=5, sticky='W')

# правая колонка цифр
pnl_right = Frame(root)
pnl_right.grid(row=1, column=5, rowspan=2, padx=10, pady=5, sticky='S')

num_height = canv_height + cell_size
canv_right = Canvas(pnl_right, width=cell_size, height=num_height, background=canv_color)
canv_right.pack()

prep_digitcells() # отрисовка цифр на правой панели

sel_digit = 0
sel_color = '#faf0be'
canv_right.bind('<1>', dig_mouse_click) # обработка клика левой кнопки мышки по правой панели
canv.bind('<1>', mouse_click) # обработка клика левой кнопки мышки по основному полю

file_name = 'Puzzle1.txt'
cells_count = row_count*col_count
f = open(file_name, 'r')
level_count = f.seek(0, 2)//cells_count
var_count.set(level_count)

# замыкание цикла
root.mainloop()

f.close()