# sqlite3 MAIN

# Перед запуском main_sqlite3 файла должна быть создана DataBase и храниться в текущей директории.
# Для создания DataBase необходимо запустить в текущей директории DB_sqlite3

# Текущая версия приложения является первой версией. MAIN содержит макет приложения. Законченная версия
# с работающим функционалом находится в Day_29.

import tkinter as tk
import tkinter.ttk as ttk # модуль ttk, содержит классы более стилизованных и современных виджетов
import engine_sqlite3

from tkcalendar import DateEntry, Calendar # pip install tkcalendar


# tk.Frame() - прямоугольная область, используется для группировки виджетов или для добавления расстояния
# между виджетами.
# tk.Label() - виджет, который отображает текст в окне и служит для информационных целей (вывод сообщений,
# подпись других элементов интерфейса). 
# .Grid() – это менеджер геометрии, который размещает виджеты в двухмерной сетке.
# .Pack() – это менеджер геометрии, который размещает виджеты по горизонтали и вертикали.

window = tk.Tk()
window.title("My APP")
#window["bg"] = "#858585" # 858585 - серый цвет в HEX
#window.geometry('600x800') # разрешение окна
window.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание по высоте или ширине)

# Создание блоков приложения
frame_add_form = tk.Frame(window, width=300, height=300) # верхний ЛЕВЫЙ блок
frame_statistic = tk.Frame(window, width=300, height=300) # верхний ПРАВЫЙ блок
frame_table = tk.Frame(window, width=600, height=300) # НИЖНИЙ блок

frame_add_form.grid(row=0, column=0, sticky="NS") # верхний ЛЕВЫЙ блок
frame_statistic.grid(row=0, column=1, sticky="NS") # верхний ПРАВЫЙ блок
frame_table.grid(row=1, column=0, columnspan=2, sticky="WE") # НИЖНИЙ блок

# Заполнение ВЕРХНЕГО ПРАВОГО блока (frame_statistic).
# l_ в имени указывает на Label()
l_most_common_text = tk.Label(frame_statistic, text="● Самые частые покупки", font="Helvetica 12")
l_most_common_value = tk.Label(frame_statistic, text=engine_sqlite3.get_most_common_item(), font="Helvetica 12 bold")
l_exp_item_text = tk.Label(frame_statistic, text="● Самая дорогая покупка", font="Helvetica 12")
l_exp_item_value = tk.Label(frame_statistic, text=engine_sqlite3.get_most_exp_item(), font="Helvetica 12 bold")
l_exp_month_text = tk.Label(frame_statistic, text="● СДП (месяц)", font="Helvetica 12")
l_exp_month_value = tk.Label(frame_statistic, text="Июль", font="Helvetica 12 bold")
l_exp_day_text = tk.Label(frame_statistic, text="● СДП(день недели)", font="Helvetica 12")
l_exp_day_value = tk.Label(frame_statistic, text="Пятница", font="Helvetica 12 bold")

l_most_common_text.grid(row=0, column=0, sticky='W', padx=10, pady=10)
l_most_common_value.grid(row=0, column=1, sticky='E', padx=10, pady=10)
l_exp_item_text.grid(row=1, column=0, sticky='W', padx=10, pady=10)
l_exp_item_value.grid(row=1, column=1, sticky='E', padx=10, pady=10)
l_exp_month_text.grid(row=2, column=0, sticky='W', padx=10, pady=10)
l_exp_month_value.grid(row=2, column=1, sticky='E', padx=10, pady=10)
l_exp_day_text.grid(row=3, column=0, sticky='W', padx=10, pady=10)
l_exp_day_value.grid(row=3, column=1, sticky='E', padx=10, pady=10)

# Заполнение ВЕРХНЕГО ЛЕВОГО блока (frame_add_form).
items = [0, 1, 2, 3, 4]
l_choose = ttk.Label(frame_add_form, text="Статья расходов", font="Helvetica 12")
f_choose = ttk.Combobox(frame_add_form, values=items)
l_amount = ttk.Label(frame_add_form, text="Сумма", font="Helvetica 12")
f_amount = ttk.Entry(frame_add_form, font="Helvetica 12", justify=tk.RIGHT)
l_date = ttk.Label(frame_add_form, text="Дата", font="Helvetica 12")
f_date = DateEntry(frame_add_form) # календарь
btn_submit = ttk.Button(frame_add_form, text="Результат")

l_choose.grid(row=0, column=0, sticky="W", padx=10, pady=10)
f_choose.grid(row=0, column=1, sticky="E", padx=10, pady=10)
l_amount.grid(row=1, column=0, sticky="W", padx=10, pady=10)
f_amount.grid(row=1, column=1, sticky="E", padx=10, pady=10)
l_date.grid(row=2, column=0, sticky="W", padx=10, pady=10)
f_date.grid(row=2, column=1, sticky="E", padx=10, pady=10)
btn_submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Заполнение НИЖНЕГО блока (frame_table).
heads = ["id", "name", "amount", "date"]
table = ttk.Treeview(frame_table, show="headings") # show="headings" убирает корневой элемент. По умолчанию show="tree headings" 
table["columns"] = heads
table["displaycolumns"] = ["id", "name", "date", "amount"] # ручное переформатироване таблицы (замена порядка именования столбцов)
for head in heads:
    table.heading(head, text=head)
    table.column(head, anchor="center")
for row in engine_sqlite3.get_table_data():
    table.insert("", tk.END, values=row)
# for row in engine_sqlite3.get_table_data(): # принудительно увеличить строки таблицы, чтобы посмотреть как работает Scrollbar
#     table.insert('', tk.END, values=row)
scroll_pane = tk.ttk.Scrollbar(frame_table, command=table.yview) # command=table.yview - когда скорллим, движемся по оси 'y' тиблицы
table["yscrollcommand"] = scroll_pane.set # необходимо для корректного отображения полосы прокрутки Scrollbar

# Необходимо сначала запаковать Scrollbar, затем запаковать таблицу
scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
table.pack()

window.mainloop()
