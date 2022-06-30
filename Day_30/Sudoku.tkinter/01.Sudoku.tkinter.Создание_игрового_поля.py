# Sudoku.tkinter 01.Создание игрового поля.

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


# определение главного окна
root = Tk()
root.title("Sudoku Game") # title (шапка) окна
root.geometry("380x380") # определение размеров окна
root.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание окна)
root_color = 'black' # цвет поля
root.configure(background=root_color)

stl = ttk.Style()
dfont = font.Font(family='helvetica', size=20)
stl.configure('.', font=dfont, background=root_color, foreground='black')

cells = []

cell_size = 40

row_count = 9
col_count = 9

canv_width = cell_size*row_count
canv_height = cell_size*col_count
canv_color = 'skyblue'
canv = Canvas(root, width=canv_width, height=canv_height, background=canv_color)
canv.pack(side='top', padx=(10,10), pady=(15,10))

prep_cells() # отрисовка ячеек
draw_lines() # отрисовка разделительныйх линий


# замыкание цикла
root.mainloop()
