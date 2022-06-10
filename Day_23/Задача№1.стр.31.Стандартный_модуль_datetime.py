# Задача№1.стр.31.Стандартная_библиотека_datetime

# Стандартная_библиотека_datetime содержт 5 классов:
# 1.datetime.datetime - для представления одновременно даты и времени.
# 2.datetime.date - для представления только даты. Содержит методы, аналогичные методам datetime для работы с датами.
# 3.datetime.time - для представления только времени. Содержит методы, аналогичные методам datetime для работы с временем.
# 4.datetime.timedelta - для представления разницы во времени. Используется для проведения арифметических операций над
# датами и аременем.
# 5.atetime.tzinfo - для представления информации о временной зоне (часовой пояс).

# Документация к модулю datetime: https://docs.python.org/3.8/library/datetime.html

# Попробуйте создать обьекты класса datetime:

# import datetime

# dt = datetime.datetime(2019,1,16)
# dt2 = datetime.datetime(2019,1,16,minute=11)
# dt3 = datetime.datetime.today()
# print(dt.replace(year=2013,hour=12))

# Попробуйте сложить дни.

# now = datetime.datetime.now()
# two_days = datetime.timedelta(2)
# in_two_days = now + two_days

# Решение:
# Обычно при использовании модуля datetime используют сокращенное название dt

import datetime as dt
from rich import print

print("[bold magenta]Program start[/]")

# моя текущая дата
today_dt = dt.datetime.today()
print(today_dt) # OUT: 2022-02-10 18:14:57.269000

# моя произвольная дата
some_d = dt.datetime(2022, 2, 10)
print(some_d) # OUT: 2022-02-10 00:00:00

# мой текущий день недели
today_wd = dt.datetime.today().weekday()
# нуменаци дней недели с нуля 0, 1, 2, 3 - это среда
print(today_wd) # OUT: 3

# моё произвольное время
some_time = dt.time(23, 15, 19)
print(some_time) # OUT: 23:15:19

# изменение даты/времени
edited_today_dt = today_dt.replace(year=2013, hour=12)
print(edited_today_dt) # OUT: 2013-02-10 12:14:57.269000

# моя текущая дата и время
some_dt = dt.datetime(2020, 12, 15, 13, 25, 9)
print(some_dt) # OUT: 2020-12-15 13:25:09

# скомбинированная дата-время
some_dt_2 = dt.datetime.combine(some_dt, some_time)
print(some_dt_2) # OUT: 2020-12-15 23:15:19
print(some_dt_2.year, some_dt_2.minute) # OUT: 2020 15

# дата и время сейчас
now_dt = dt.datetime.now()
print(now_dt) # OUT: 2022-02-10 18:21:12.749000

# дельта (интервал) времени
delta_time1 = dt.timedelta(seconds=10, weeks=2)
print(delta_time1) # OUT: 14 days, 0:00:10
print(delta_time1.days) # OUT: 14
print(delta_time1.total_seconds()) # OUT: 1209610.0

# дельта (интервал) времени
delta_time2 = dt.timedelta(days=-10)
print(delta_time2) # OUT: -10 days, 0:00:00

# текущее время, только завтра
print(dt.datetime.now() + dt.timedelta(days=1)) # OUT: 2022-02-11 18:26:11.322000

# !!!так нельзя прибавлять!!! к dt.datetime.now() можно прибавить промежутки времени
# print(dt.datetime.now() + dt.datetime.now())

# сложение дней
print(dt.timedelta(days=1) + dt.timedelta(days=1)) # OUT: 2 days, 0:00:00

# вывод данных в терминал методом f строки
now = dt.datetime.now()
print(f'{now.day} day, {now.hour}:{now.minute}') # OUT: 10 day, 18:29

# Python сам отформатирует полученные данные в результате умножения, 10 дней, 70 часов = 12 дней, 22 часа
print(dt.timedelta(days=1, hours=7) * 10) # OUT: 12 days, 22:00:00

# Python сам отформатирует полученные данные в результате деления
print(dt.timedelta(days=1, hours=7) / dt.timedelta(days=1)) # OUT: 1.2916666666666667

# посчитем интервал времени
my_dt = dt.datetime(2023, 12, 15, 13, 25, 9)
now = dt.datetime.now()
print(my_dt - now) # OUT: 672 days, 18:39:47.762000

print("[bold magenta]Program finish[/]")

input()
