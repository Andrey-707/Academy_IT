# pymysql MAIN

# Перед запуском main_pymysql файла должна быть создана DataBase и храниться на сервере.
# Нужно создать DataBase на сервере, затем для заполнения необходимо запустить в текущей директории
# DB_pymysql

# Текущая версия приложения является завершенной на текущий момент и содержит основной функционал.

import tkinter as tk
import tkinter.ttk as ttk # модуль ttk, содержит классы более стилизованных и современных виджетов
import pymysql
import engine_pymysql

from config import host, port, user, password, database
from tkcalendar import DateEntry, Calendar # pip install tkcalendar
from rich import print


# !!! Поскольку База Данных pymysql разворачивается на сервере, то для работы программы необходимо включить
# Open Server Panel, затем запустить (справа в трее ЗЕЛЕНЫЙ флажок) !!!

# tk.Frame() - прямоугольная область, используется для группировки виджетов или для добавления расстояния между виджетами.
# tk.Label() - виджет, который отображает текст в окне и служит для информационных целей (вывод сообщений, подпись других элементов
# интерфейса). 
# .Grid() – это менеджер геометрии, который размещает виджеты в двухмерной сетке.
# .Pack() – это менеджер геометрии, который размещает виджеты по горизонтали и вертикали.

def create_upper_legt():
    """Заполнение ВЕРХНЕГО ЛЕВОГО блока (в границах frame_add_form)"""
    global items, f_choose, f_amount, f_date

    items = engine_pymysql.get_all_expenses_items()
    l_choose = tk.Label(frame_add_form, text="● Виды затрат", font=fontExample, bg="#000", fg="#fff")
    f_choose = ttk.Combobox(frame_add_form, values=engine_pymysql.get_all_expenses_items()["names"],
                            font=fontExample, justify=tk.RIGHT, state="normal") # выпадающий список values=
    f_choose.configure(background="#000", foreground="#fff")
    l_amount = tk.Label(frame_add_form, text="● Сумма", font=fontExample, bg="#000", fg="#fff")
    f_amount = ttk.Spinbox (frame_add_form, from_=0.0, to=1000000.0, increment=1.0, font=fontExample, justify=tk.RIGHT,
                            background="#000", foreground="#fff")
    l_date = tk.Label(frame_add_form, text="● Дата", font=fontExample, bg="#000", fg="#fff")
    f_date = DateEntry(frame_add_form, date_pattern="YYYY-mm-dd", font=fontExample) # формат вывода времени date_pattern="YYYY-mm-dd"
    btn_submit = tk.Button(frame_add_form, text="Добавить", command=form_submit)
    btn_submit.config(bg="#000", fg="#fff", font=fontExample, bd=2) # настройки кнопки "Добавить"
    btn_cancel = tk.Button(frame_add_form, text="Отменить", command=form_cancel)
    btn_cancel.config(bg="#000", fg="#fff", font=fontExample, bd=2) # настройки кнопки "Отменить"

    l_choose.grid(row=0, column=0, padx=0, pady=10, sticky="W") # padx, pady - отступы по оси x и y соответственно
    f_choose.grid(row=0, column=1, padx=0, pady=10, sticky="E") # sticky - прилипание к полюсам ("E" - восток)
    l_amount.grid(row=1, column=0, padx=0, pady=10, sticky="W")
    f_amount.grid(row=1, column=1, padx=0, pady=10, sticky="E")
    l_date.grid(row=2, column=0, padx=0, pady=10, sticky="W")
    f_date.grid(row=2, column=1, padx=0, pady=10, sticky="E")
    btn_cancel.grid(row=3, column=0, padx=0, pady=10, sticky="W")
    btn_submit.grid(row=3, column=1, padx=0, pady=10, sticky="E")


def create_upper_right():
    """Заполнение ВЕРХНЕГО ПРАВОГО блока (в границах frame_statistic)"""
    global l_most_common_value, l_exp_item_value, l_exp_month_value, l_exp_day_value

    l_most_common_text = tk.Label(frame_statistic, text="● Самые частые покупки", font=fontExample, bg="#000", fg="#fff")
    l_most_common_value = tk.Label(frame_statistic, text=engine_pymysql.get_most_common_item(), font=fontExample, bg="#000", fg="#fff")
    l_exp_item_text = tk.Label(frame_statistic, text="● Самая дорогая покупка", font=fontExample, bg="#000", fg="#fff")
    l_exp_item_value = tk.Label(frame_statistic, text=engine_pymysql.get_most_exp_item(), font=fontExample, bg="#000", fg="#fff")
    l_exp_month_text = tk.Label(frame_statistic, text="● Месяц самой дорогой покупки", font=fontExample, bg="#000", fg="#fff")
    l_exp_month_value = tk.Label(frame_statistic, text=engine_pymysql.get_most_exp_month(), font=fontExample, bg="#000",fg="#fff")
    l_exp_day_text = tk.Label(frame_statistic, text="● День самой дорогой покупки", font=fontExample, bg="#000", fg="#fff")
    l_exp_day_value = tk.Label(frame_statistic, text=engine_pymysql.get_most_exp_day(), font=fontExample, bg="#000", fg="#fff")

    l_most_common_text.grid(row=0, column=0, padx=0, pady=10, sticky="W")
    l_most_common_value.grid(row=0, column=1, padx=0, pady=10, sticky="E")
    l_exp_item_text.grid(row=1, column=0, padx=0, pady=10, sticky="W")
    l_exp_item_value.grid(row=1, column=1, padx=0, pady=10, sticky="E")
    l_exp_month_text.grid(row=2, column=0, padx=0, pady=10, sticky="W")
    l_exp_month_value.grid(row=2, column=1, padx=0, pady=10, sticky="E")
    l_exp_day_text.grid(row=3, column=0, padx=0, pady=10, sticky="W")
    l_exp_day_value.grid(row=3, column=1, padx=0, pady=10, sticky="E")


def form_submit():
    """Подключается к БД, добавляет данные в конец БД, собирает приложение заново"""
    global scroll_pane, table

    id_ = engine_pymysql.get_id() + 1 # номер id = последний нормер +1
    amount = float(f_amount.get()) # сумма в формате числа с плавающей точкой
    payment_date = engine_pymysql.get_timestamp_from_string(f_date.get()) # дата YYYY-mm-dd
    expense_id = items["accordance"][f_choose.get()] # items см. в функции create_upper_legt()

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"[bold blue]Подключение к БД <<{database}>>...[/]")

    with connection.cursor() as cursor:
        # !!! В pymysql ИСПОЛЬЗУЕТСЯ ПЕРЕДАЧА ЗНАЧЕНИЙ VALUES В ФОРМАТЕ %s !!!
        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (%s, %s, %s, %s);" # добавление данных с использованием переменных
        cursor.execute(query, (id_, amount, payment_date, expense_id))
        connection.commit()
        print(f"[bold green]Данные добавлены[/]")

    # собрать приложение заново
    update()


def form_cancel():
    """Подключается к БД, удаляет последние данные из БД (по индексу), собирает приложение заново"""
    id_ = engine_pymysql.get_id()

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"[bold blue]Подключение к БД <<{database}>>...[/]")

    with connection.cursor() as cursor:
        # !!! В pymysql ИСПОЛЬЗУЕТСЯ ПЕРЕДАЧА ЗНАЧЕНИЙ В ФОРМАТЕ %s !!!
        delete = "DELETE FROM payments WHERE payments.id = %s;" # удаление данных с использованием переменной
        cursor.execute(delete, (id_, ))
        connection.commit()
        print(f"[bold red]Данные удалены[/]")

    # собрать приложение заново
    update()


def fixed_map(option):
    """Решение проблемы с подсветкой строк на Python 3.8
    Взято отсюда: https://bugs.python.org/issue36468
    Используется в main функции для настррйки Treeview"""
    return [elm for elm in style.map("Treeview", query_opt=option) if elm[:2] != ("!disabled", "!selected")]


def create_lower():
    """Заполнение НИЖНЕГО блока (в границах frame_table)"""
    global scroll_pane, table, style

    # настройки "Treview"
    style = ttk.Style()
    style.map("Treeview", foreground=fixed_map("foreground"), background=fixed_map("background"))
    style.configure("Treeview", rowheight=25, font="Helvetica 12")

    heads = ["id", "name", "amount", "date"]
    table = ttk.Treeview(frame_table, show="headings", columns=heads, height=11, padding=0, selectmode="none") # show="headings" убирает корневой элемент. По умолчанию show="tree headings" 
    
    # Создание тага для выделение строки таблицы
    table.tag_configure("black", background="#000", foreground="#fff")
    table.tag_configure("white", background="#fff", foreground="#000")

    #table["columns"] = heads # ручное переформатироване таблицы (замена имен заголовков столбцов)
    table["displaycolumns"] = ["id", "name", "date", "amount"] # ручное переформатироване таблицы (замена порядка именования столбцов)
    root_item = table.insert("", tk.END, text="root", open=True, tag="black") # open=True - список раскрыт

    # Именование столбцов таблицы
    for head in heads:
        table.heading(head, text=head)
        table.column(head, anchor="center")

    # Заполнение таблицы строками с использованием перевода даты из абсолютной величины в формат YYYY-mm-dd
    for row in engine_pymysql.get_table_data():
        rrow = []
        for i, j in enumerate(row):
            if j not in rrow :
                if i == 3: # i == 3 - это индекст колонны payment_date
                    rrow.append(engine_pymysql.get_date(j))
                else:
                    rrow.append(j)
            elif i != j:
                rrow.append(j)
        table.insert(root_item, tk.END, values=rrow, tag="black")

    # Дополнительные строки тиблицы (БЕЗ ПЕРЕВОДА ДАТЫ, ФОН - БЕЛЫЙ)

    # # Выведем конкретный номер строки (номер 7)
    # for i, row in enumerate(engine_sqlite3.get_table_data()):
    #     if i == 7:
    #         table.insert("", tk.END, values=row, tag="white")
    #     else:
    #         pass

    # Выведем строку с максимальное значение цены
    max_amount = 0
    for i, row in enumerate(engine_pymysql.get_table_data()):
        if row[2] > max_amount:
            max_amount = row[2]

    for i, row in enumerate(engine_pymysql.get_table_data()):
        if row[2] == max_amount:
            table.insert("", tk.END, values=row, tag="white")

    # Scrollbar
    scroll_pane = ttk.Scrollbar(frame_table, command=table.yview) # command=table.yview - когда скорллим, движемся по оси 'y' тиблицы
    table["yscrollcommand"] = scroll_pane.set # необходимо для корректного отображения полосы прокрутки Scrollbar
    
    # Необходимо сначала запаковать Scrollbar, затем запаковать таблицу
    scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack()


def update():
    """Убивает приложение после внесения изменений  в тиблицу. Собирает его заново"""
    tasks = [l_most_common_value, l_exp_item_value, l_exp_month_value, l_exp_day_value, table, scroll_pane]
    for task in tasks:
        task.destroy()

    # Перезапуск конструктора
    create_upper_right()
    create_upper_legt()
    create_lower()


def main():
    """Главная функция приложение (КОНСТРУКТОР)"""
    global window, frame_add_form, frame_statistic, frame_table, fontExample, img_, style

    window = tk.Tk()
    window.title("Purse (pymysql)") # шапка
    window.wm_attributes("-alpha", 0.95) # прозрачность окна 5%
    window["bg"] = "#000000" # черный цвет в HEX
    window.geometry('825x496') # разрешение окна
    window.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание по высоте или ширине)
    
    # Иконка в шапке
    window.iconphoto(True, tk.PhotoImage(
        file=r"icon\icon.png"))

    # если нужно установить картинку холста
    # img_ = tk.PhotoImage(file=r"путь_к_картинке\имя_картинки.png")
    
    # Шаблон текста
    fontExample = ("Helvetica", 10, "bold")

    # Создание рамок для блоков приложения
    frame_add_form = tk.Frame(window,  width=400, height=400, bd=0) # геометрия рамки
    frame_add_form.config(bg="#000000")
    frame_add_form.place(relx=0, rely=0, relwidth=1, relheight=1) # расположение рамки
    frame_add_form.grid(row=0, column=0, padx=(0,0), pady=(0,0), sticky="NS") # верхняя левая рамка

    frame_statistic = tk.Frame(window, width=400, height=400, bd=0) # геометрия рамки
    frame_statistic.config(bg="#000000")
    frame_statistic.place(relx=0, rely=0, relwidth=1, relheight=1) # расположение рамки
    frame_statistic.grid(row=0, column=1, padx=(0,0), pady=(0,0), sticky="NS") # верхняя правая рамка

    frame_table = tk.Frame(window, width=800, height=400, bd=0) # геометрия рамки
    frame_table.config(bg="#000000")
    frame_table.place(relx=0, rely=0, relwidth=1, relheight=1) # расположение рамки
    frame_table.grid(row=1, column=0, padx=(0,0), pady=(0,0), columnspan=2, sticky="WE") # нижняя рамка

    # Конструктор
    create_upper_right()
    create_upper_legt()
    create_lower()

    # Цикл
    window.mainloop()

if __name__ == "__main__":
    main()
    