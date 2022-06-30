# Sudoku.tkinter 02.Добавление интерфейса.

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
            row.append([rect])
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
        rect = canv_right.create_rectangle(x_beg, y_beg, x_end, y_end, fill=canv_color)
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
    pass

def fnc_clear():
    """
    Очищает игровое поле.
    """
    pass


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

# кнопка загрузки уровня
btn_width = 8
btn_load = Button(root, text='Load', width=btn_width, command=fnc_load)
btn_load.config(background='black', foreground='white', font=sym_font, bd=2)
btn_load.grid(row=3, column=0, padx=(15,0), pady=5, sticky='W')

# кнопка очистки уровня
btn_width = 8
btn_load = Button(root, text='Clear', width=btn_width, command=fnc_clear)
btn_load.config(background='black', foreground='white', font=sym_font, bd=2)
btn_load.grid(row=3, column=1, padx=(100,5), pady=5, sticky='W')

# правая колонка цифр
pnl_right = Frame(root)
pnl_right.grid(row=1, column=5, rowspan=2, padx=10, pady=5, sticky='S')

num_height = canv_height + cell_size
canv_right = Canvas(pnl_right, width=cell_size, height=num_height, background=canv_color)
canv_right.pack()

prep_digitcells() # отрисовка цифр

# замыкание цикла
root.mainloop()