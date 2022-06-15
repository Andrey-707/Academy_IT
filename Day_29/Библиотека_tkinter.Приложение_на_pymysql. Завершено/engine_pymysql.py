# sqlite3 ENGINE

import pymysql
import datetime

from config import host, port, user, password, database # импортрем конфиги
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


def get_date(tms):
    """Преобразует дату"""
    # print(datetime.datetime.fromtimestamp(tms)) # формат 2020-09-05 00:00:00
    # print(datetime.datetime.fromtimestamp(tms).date()) # формат 2020-09-05
    return datetime.datetime.fromtimestamp(tms).date()


def get_most_exp_day():
    """Запускает получение данных из БД, возвращает день недели и дату, в который была совершена самая дорогая покупка"""
    data = get_statistic_data()
    weak_days = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    max_ = max(data, key=lambda x: x["amount"])["payment_date"] # величина amount key=1, дата key=2

    #print(get_date(max_).weekday())
    return weak_days[get_date(max_).weekday()], "-", get_date(max_) # возвращает день недели и дату


def get_most_exp_month():
    """Запускает получение данных из БД, возвращает месяц, в который была совершена самая дорогая покупка"""
    data = get_statistic_data()
    month = ("0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
              "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
    max_ = max(data, key=lambda x: x["amount"])["payment_date"] # величина amount key=1, дата key=2
    date = get_date(max_)

    # print(month[max_.month])
    return month[date.month]


def get_all_expenses_items():
    """Подключается к БД, получает данные, возвращает тип статьи затрат в виде списка"""
    all_data = {"accordance": {}, "names": []}
    result = {}
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"[bold blue]Подключение к БД <<{database}>>...[/]")

    with connection.cursor() as cursor:
        query = "SELECT id, name FROM expenses;"
        cursor.execute(query)
        for i in list(cursor):
            result[i["id"]] = i["name"]

        #print(result)

        # all_data = [categor["id"] for categor in cursor]
    all_data["accordance"] = {result[k]: k for k in result}
    all_data["names"] = [v for v in result.values()]

    # print(all_data)
    return all_data


def get_timestamp(y, m, d):
    """Преобразует время"""
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_timestamp_from_string(s):
    """Преобразует время"""
    t = s.split('-')

    return int(get_timestamp(int(t[0]), int(t[1]), int(t[2])))


def get_id():
    """Получить последний порядковый номер id"""
    data = get_statistic_data()
    id_ = list(data)[-1]["id"]
    #print(id_, type(id_))
    
    return id_
