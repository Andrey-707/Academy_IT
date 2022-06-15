# sqlite3 ENGINE

# ENGINE файл содержит основной функционал приложения.
# Расширения DataBase: .db, .db3, .sqlite, .sqlite3

import sqlite3
import datetime

from rich import print


def get_statistic_data():
    """Подключается к БД, получает данные, возвращает тип дпнных <class 'pymysql.cursors.DictCursor'>"""
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        # объединение двух таблиц по id, результатом будет к примеру для интернета: (2, 12.0, 1598907600, 3, 3, 'Интернет')
        query = """SELECT * FROM payments JOIN expenses
                ON expenses.id = payments.expense_id;"""
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
        new_list.append((row[0], row[5], row[1], row[2]))
    
    # print(new_list)
    return new_list


def get_most_common_item():
    """Запускает получение данных из БД, возвращает имя наиболее частой покупки"""
    data = get_statistic_data()
    quantity = {}
    for pay in data:
    # итерация по data, каждый элемент pay по типу данных будет <class 'dict'>
        # print(pay, type(pay))
        # print(quantity)
        # print(pay["expense_id"])
        if pay[3] in quantity:
            quantity[pay[3]]['gty'] += 1 # по key "gty" увелививет value на 1
        else:
            quantity[pay[3]] = {'gty': 1, 'name': pay[5]} # создает словарь, key = "expense_id", value будет комуналка, топливо или интернет, например = {'gty': 1, 'name': 'Комуналка'}

    return max(quantity.values(), key=lambda x: x['gty'])['name']


def get_most_exp_item():
    """Запускает получение данных из БД, возвращает имя наиболее дорогой покупки"""
    data = get_statistic_data()

    return max(data, key=lambda x: x[1])[5]
