# sqlite3 ENGINE

import pymysql
import datetime

from config import host, port, user, password, database # импортируем конфиги
from rich import print


def get_statistic_data():
    """Подключается к БД, получает данные, возвращает тип дпнных <class 'pymysql.cursors.DictCursor'>"""
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"[bold blue]Подключение к БД <<{database}>>...[/]")

    with connection.cursor() as cursor:
        query = "SELECT * FROM payments JOIN expenses ON expenses.id = payments.expense_id;"
        cursor.execute(query)
        print(f"[bold yellow]Данные получены[/]")

    # print(cursor, type(cursor))
    return cursor


def get_table_data():
    """Запускает получение данных из БД, возвращает данные в виде писка"""
    data = get_statistic_data()
    new_list = []
    for row in data:
        # print(row)
        new_list.append((row["id"], row["name"], row["amount"], row["payment_date"]))
    
    # print(new_list)
    return new_list


def get_most_common_item():
    """Запускает получение данных из БД, возвращает имя наиболее частой покупки"""
    data = get_statistic_data()
    quantity = {}
    # итерация по data, каждый элемент pay по типу данных будет <class 'dict'>
    for pay in data:
        # print(pay, type(pay))
        # print(quantity)
        # print(pay["expense_id"])
        if pay["expense_id"] in quantity:
            quantity[pay["expense_id"]]["gty"] += 1 # по key "gty" увелививет value на 1
        else:
            quantity[pay["expense_id"]] = {"gty": 1, "name": pay["name"]} # создает словарь, key = "expense_id", value будет комуналка, топливо или интернет, например = {'gty': 1, 'name': 'Комуналка'}
       
    return max(quantity.values(), key=lambda x: x["gty"])["name"]


def get_most_exp_item():
    """Запускает получение данных из БД, возвращает имя наиболее дорогой покупки"""
    data = get_statistic_data()

    return max(data, key=lambda x: x["id"])["name"]
