# Создание DataBase на sqlite3

import sqlite3

from rich import print

# !!! Поскольку База Данных sqlite3 НЕ разворачивается на сервере, то для работы программы НЕ нужно
# включить Open Server Panel. Программа создает в директории файл database.db !!!

# пошагово раскоментировать строчки query и применить cursor.execute(query)
try:
    # Создать таблицу `payments` в БД "database.db" (IF NOT EXISTS == ЕСЛИ НЕ СУЩЕСТВУЕТ)
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = "CREATE TABLE IF NOT EXISTS payments(id INTEGER, amount REAL, payment_date INTEGER, expense_id INTEGER);" # REAL == float
        cursor.execute(query)
        print("[bold magenta]Создание таблицы `payments` в БД <<database.db>>")

    # Добавление новых данных в таблицу `payments`
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (1, 120.0, 1598907600, 1);" # 1598907600 - это количество секунд, начиная с 1970 года 
        cursor.execute(query)
        count = 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (2, 12.0, 1598907600, 3);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (3, 20.0, 1598907600, 2);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (4, 20.0, 1598994000, 2);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (5, 20.0, 1599080400, 2);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (6, 20.0, 1599166800, 2);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (7, 20.0, 1599253200, 2);"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

    # Создать таблицу `expenses` в БД "database.db"
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = "CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT);"
        cursor.execute(query)
        print("[bold magenta]Создание таблицы `expenses` в БД <<database.db>>[/]")

    # Добавление новых данных в таблицу `expenses`
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        count = 1
        query = "INSERT INTO expenses(id, name) VALUES (1, 'Коммуналка');"
        cursor.execute(query)
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

        count += 1
        query = "INSERT INTO expenses(id, name) VALUES (2, 'Топливо');"
        cursor.execute(query)
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

        count += 1
        query = "INSERT INTO expenses(id, name) VALUES (3, 'Интернет');"
        cursor.execute(query)
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

    # with sqlite3.connect('database.db') as db:
    #     cursor = db.cursor()

    #     # Удалить таблицу `payments` из БД "database.db"
    #     query = "DROP TABLE `payments`"
    #     cursor.execute(query)
    #     print(f"[bold red]Удаление таблицы `payments` из БД <<database.db>>[/]")

    #     # Удалить таблицу `expenses` из БД "database.db"
    #     query = "DROP TABLE `expenses`"
    #     cursor.execute(query)
    #     print(f"[bold red]Удаление таблицы `expenses` из БД <<database.db>[/]")

except Exception as ex:
    print("Ошибка при подключении к БД:")
    print(ex)
