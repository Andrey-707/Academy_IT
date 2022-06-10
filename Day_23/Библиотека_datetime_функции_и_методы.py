# Документация к модулю datetime: https://docs.python.org/3.8/library/datetime.html
# Классы, предоставляемые модулем datetime:
import datetime

from rich import print


print("[bold magenta]Program start[/]")

# Класс datetime.date(year, month, day) - стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.
# OUT: 2021-12-27
print(datetime.date(2021, 12, 27))

# Класс datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - стандартное время, не зависит от даты.
# Атрибуты: hour, minute, second, microsecond, tzinfo.
# OUT: 00:00:00
print(datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None))

# Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.
# OUT: 24 days, 0:00:00
print(datetime.timedelta(24))
# OUT: 0:00:24
print(datetime.timedelta(0, 24))

# Класс datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового
# пояса и / или летнего времени).
# OUT: <class 'datetime.tzinfo'>
print(datetime.tzinfo)

# Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбинация даты
# и времени.
# Обязательные аргументы:

# datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999)
# 1 ≤ month ≤ 12
# 1 ≤ day ≤ количество дней в данном месяце и году
# Необязательные:

# 0 ≤ minute < 60
# 0 ≤ second < 60
# 0 ≤ microsecond < 1000000
# OUT: 2021-12-27 00:00:00
print(datetime.datetime(2021, 12, 27, hour=0, minute=0, second=0, microsecond=0, tzinfo=None))

# Методы класса datetime:

# datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением
# tz=None.
# OUT: 28:12:2021
print(datetime.date.today().strftime("%d:%m:%Y"))

# datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
# OUT: 2020-09-07 03:00:00
print(datetime.datetime.fromtimestamp(52 * 356 * 86400))

# datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
ordinal = 123456
date = datetime.date.fromordinal(ordinal)
# OUT: The Gregorian date for the Gregorianordinal 123456 is: 0339-01-05
print("The Gregorian date for the Gregorianordinal %d is: %s"%(ordinal, date))

# datetime.now(tz=None) - объект datetime из текущей даты и времени.
timezone_offset = -8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))
# OUT: 2021-12-27 17:32:27.566000-08:00
print(datetime.datetime.now(tzinfo))

# datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
# OUT: 2021-12-27 00:00:00
print(datetime.datetime.combine(datetime.date(2021, 12, 27), datetime.time(0, 0)))

# datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
# OUT: 2021-12-27 00:00:00
print(datetime.datetime.strptime("27 December, 2021", "%d %B, %Y"))

# datetime.strftime(format) - см. функцию strftime из модуля time.
# OUT: 12/28/2021, 04:43:45
print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

# datetime.date() - объект даты (с отсечением времени).
# OUT: 2021-12-27
print(datetime.date(2021, 12, 27))

# datetime.time() - объект времени (с отсечением даты).
# OUT: 04:46:00
print(datetime.time(4, 46, 00))

# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый
# объект datetime с изменёнными атрибутами.
# OUT: 2000-12-28
print(datetime.date.today().replace(year=2000))

# datetime.timetuple() - возвращает struct_time из datetime.
# OUT: time.struct_time(tm_year=2021, tm_mon=12, tm_mday=28, tm_hour=4, tm_min=58,
#      tm_sec=38, tm_wday=1, tm_yday=362, tm_isdst=-1)
print(datetime.datetime.today().timetuple())

# datetime.toordinal() - количество дней, прошедших с 01.01.1970.
# OUT: 738152
print(datetime.date.today().toordinal())

# datetime.timestamp() - возвращает время в секундах с начала эпохи.
# OUT: 1640657063.636
print(datetime.datetime.today().timestamp())

# datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
# OUT: Tuesday
print(datetime.datetime.today().strftime('%A'))
# OUT: 0
print(datetime.date(2021,12,27).weekday())

# datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
# OUT: 1
print(datetime.date(2021,12,27).isoweekday())

# datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
# OUT: ISO Date:(2020, 1, 3)
print("ISO Date:{}".format(datetime.datetime(2020, 1, 1, 0, 0, 0).isocalendar()))

# datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
# OUT: 2021-12-28T02:25:17.907000
print(datetime.datetime.utcnow().isoformat(sep='T'))

# datetime.ctime() - см. ctime() из модуля time.
# OUT: Mon Dec 27 00:00:00 2021
print(datetime.date(2021, 12, 27).ctime())

print("[bold magenta]Program finish[/]")

input()
