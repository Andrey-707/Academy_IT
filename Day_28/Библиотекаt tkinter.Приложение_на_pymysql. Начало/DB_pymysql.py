import pymysql

from config import host, port, user, password, database # импортируем конфиги
from rich import print

# Зайти в PHP MyAdmin, создать новую (пустую) БД с именем "database", затем запустить файл DB_pymysql.py
# чтобы заполнить БД "database" данными.
try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"[bold blue]Подключение к БД <<{database}>>...[/]")

    # Создать таблицу `payments` в БД "database" (IF NOT EXISTS == ЕСЛИ НЕ СУЩЕСТВУЕТ)
    with connection.cursor() as cursor:
        query = "CREATE TABLE IF NOT EXISTS payments(id INT, amount REAL, payment_date INT, expense_id INT, PRIMARY KEY (id));"
        cursor.execute(query)
        print(f"[bold magenta]Создание таблицы `payments` в БД <<{database}>>[/]")

    # Добавление новых данных в таблицу `payments`
    with connection.cursor() as cursor:
        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (1, 120.0, 1598907600, 1);"
        cursor.execute(query)
        count = 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`[/]")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (2, 12.0, 1598907600, 3);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (3, 20.0, 1598907600, 2);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (4, 20.0, 1598994000, 2);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (5, 20.0, 1599080400, 2);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (6, 20.0, 1599166800, 2);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        query = "INSERT INTO payments(id, amount, payment_date, expense_id) VALUES (7, 20.0, 1599253200, 2);"
        cursor.execute(query)
        count +=1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `payments`")

        # Отправить данные на сервер
        connection.commit()
        print("[bold yellow]Отправка данных на сервер[/]")

    # Создать таблицу `expenses` в БД "database"
    with connection.cursor() as cursor:
        query = "CREATE TABLE IF NOT EXISTS expenses(id INT, name VARCHAR(32), PRIMARY KEY (id));"
        cursor.execute(query)
        print(f"[bold magenta]Создание таблицы `expenses` в БД <<{database}>>[/]")

    # Добавление новых данных в таблицу `expenses`
    with connection.cursor() as cursor:
        query = "INSERT INTO expenses(id, name) VALUES (1, 'Коммуналка');"
        cursor.execute(query)
        count = 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

        query = "INSERT INTO expenses(id, name) VALUES (2, 'Топливо');"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

        query = "INSERT INTO expenses(id, name) VALUES (3, 'Интернет');"
        cursor.execute(query)
        count += 1
        print(f"[bold cyan]{count}.Добавление данных в таблицу `expenses`[/]")

        # Отправить данные на сервер
        connection.commit()
        print("[bold yellow]Отправка данных на сервер[/]")

    
    # with connection.cursor() as cursor:
    #     # Удалить таблицу `payments` из БД "database"
    #     query = "DROP TABLE `payments`"
    #     cursor.execute(query)
    #     print(f"[bold red]Удаление таблицы `payments` из БД <<{database}>>[/]")
        
    #     # Удалить таблицу `expenses` из БД "database.db"
    #     query = "DROP TABLE `expenses`"
    #     cursor.execute(query)
    #     print(f"[bold red]Удаление таблицы `expenses` из БД <<{database}>>[/]")

except Exception as ex:
    print("Ошибка при подключении к БД:")
    print(ex)
