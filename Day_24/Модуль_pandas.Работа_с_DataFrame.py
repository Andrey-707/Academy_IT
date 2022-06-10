# Модуль_pandas. Работа с DataFrame

import numpy as np
import pandas as pd

from rich import print


# двумерный массив с персональными данными
l = [['Anna', 23, 3],
     ['Sam', 36, 10],
     ['Bill', 33, 7],
     ['Moica', 23, 7],
     ['Anna', 27, 7],
     ['Peter', 32, None]]
# print(l)

df = pd.DataFrame(l)
"""OUT:
       0   1     2
0   Anna  23   3.0
1    Sam  36  10.0
2   Bill  33   7.0
3  Moica  23   7.0
4   Anna  27   7.0
5  Peter  32   NaN
"""
# print(df)


# Таблицы в pandas - это DataFrame
# print(type(df)) # OUT: <class 'pandas.core.frame.DataFrame'>

# Выведем на печать содержимое столбцов таблицы
# print(df[0]) # В строке <<Name: 0, dtype: object>> object == str
# print(df[1]) # В строке <<Name: 1, dtype: int64>> int64 == int
# print(df[2]) # В строке <<Name: 2, dtype: float64>> float64 == float

# Каждый столбец (подтабличка) в pandas - это Series
# print(type(df[2])) # OUT: <class 'pandas.core.series.Series'>

# именование колонн (столбцов) и именование строк
df.columns = ['name', 'age', 'expr'] # именование колонн (столбцов)
df.index = ['a', 'b', 'c', 'd', 'e', 'f'] # именование строк
"""OUT:
    name  age  expr
a   Anna   23   3.0
b    Sam   36  10.0
c   Bill   33   7.0
d  Moica   23   7.0
e   Anna   27   7.0
f  Peter   32   NaN
"""
# print(df)

# команда печатает колонну 'name'
# print(df['name'])

# можно преобразовать Series к списку
# print(list(df['name'])) # OUT: ['Anna', 'Sam', 'Bill', 'Moica', 'Anna', 'Peter']

# Переименование строк. Строки принимают имена столбца 'name'
df.index = df['name'] # НЕ КОМЕНТИРОВАТЬ. ИЛИ КОД НИЖЕ БУДЕТ ВЫБРАСЫВАТЬ ИСКЛЮЧЕНИЯ !!!
# print(df)

# Командой df.loc - можно обращаться если столбцы и колонны именю имена, а df.iloc - обращение по индексам
# print(df.iloc[1, 1]) # обращаемся по индексам 1, 1. Получаем 36
# print(df.loc['b', 'age']) # обращаемся по именан 'b', 'age'. Если не переименован столбец, получаем 36
# print(df.loc["Sam", 'age']) # KeyError: 'Sam'. Если закоментирован код на строке 63 <<df.index = df['name']>>

# Срез таблицы. Выводим на печать часть таблицы
# print(df.iloc[1:2+1])
# print(df.iloc[2:5+1])
# print(df.iloc[1:3+1, 1])
# print(df.iloc[1:3+1, 0:1+1])

# выводим на печать часть таблицы, но обращаемся по именам (двоеточие указывает на диапазон)
# print(df.loc['Sam':'Peter'])
# print(df.loc['Sam':'Peter', 'name':'age'])

# выводим часть таблицы, но обращаемся по именам (запятая - НЕ диапазон, а перечисление)
# print(df.loc[['Sam', 'Peter'], ['name', 'expr']])

# print(df.loc['Anna']) # Выводим информацию по двум именам 'Anna', т.к. имена не уникальны

# НЕ РАБОТАЕТ, Т.К. КЛЮЧ НЕ УНИКАЛЕН
# print(df.loc['Anna': 'Bill']) # KeyError: "Cannot get left slice bound for non-unique label: 'Anna'"

# НЕ РАБОТАЕТ, Т.К. ПЕРЕДАЕМ НЕ СПИСОК
# print(df.loc['Anna', 'Bill']) # KeyError: 'Bill'
# print(df.loc[['Anna', 'Bill']]) # А ТАК РАБОТАЕТ

# df.info() # информация по таблице
"""OUT:
<class 'pandas.core.frame.DataFrame'>
Index: 6 entries, Anna to Peter
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    6 non-null      object
 1   age     6 non-null      int64
 2   expr    5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 192.0+ bytes
"""

# в .shape хранится количество строк и столбцов (6, 3) .shape[0] столбцы - 6 .shape[1] строки - 3
# print(df.shape, df.shape[0], df.shape[1])

# describe == описывать
# print(df.describe())
# Разшифруем .describe():
# count - количетсво элементов; mean - среднее значение; std -стандартное отклонение (разброс);
# min - минимум; 25%, 50%, 75% - квантали; 50% - медиана; max - максимум.

# print(type(df.describe())) # тип данных <class 'pandas.core.frame.DataFrame'>
# print(df.describe()['age']) # описывать столбец 'age'
# print(type(df.describe()['age'])) # тип данных <class 'pandas.core.series.Series'>

# print(df)
# print(list(df['name']))

# Переименование столбцов и строк
# df.rename(columns={'age': 'X'}, inplace=True) # переименование столбца 'age'
# print(df)

# переименование столбцов 'X' и 'expr' (axis=1 Если 1, то переименовываются стоки) если не указать
# inplace=True, переименовать не получится
# df.rename({'X': 'age', 'expr': 'exp'}, axis=1, inplace=True)
# print(df)

 # переименование строки 'Bill' (axis=0 Если 0, то работаем по индексам)
# df.rename({'Bill': 'Tom'}, axis=0, inplace=True)
# print(df)

# Работа с Series:
# print(df['age'] + 1) # вывести на печать столбец 'age' и добавить к значениям 'age' 1
# print(df['age'] ** 2) # вывести на печать столбец 'age' и возвести значения 'age' в стеень 2
# print(df['age'] == 33) # сравнение 'age' со значением 33 # OUT: Bill      True
# print(df[df['age'] == 33]) # создаем <<маску>> df['age'] == 33, обращаемся к таблице  и выводим данные 
# print(df['expr'] >= 7) # выводит True для тех, у кого опыт работы >= 7
# print(df[df['expr'] >= 7]) # создаем <<маску>> df['expr'] >= 7, обращаемся к таблице  и выводим данные 

# df['gender'] = [0, 1, 1, 1, 0, 1] # создать новый столбец 'gender', значения будут данными из списка
# print(df)

# df['metro'] = 'M' # создать новый столбец 'metro' со значениями 'M'
# print(df)

# df['new_age'] = df['age'] + 1 # создать новый столбец 'new_age', в котором возраст увеличился на 1
# print(df)

# df['double_age'] = df['age'] + df['age'] # создать новый столбец 'double_age', в котором значение удвоено
# print(df)

# print(df.append({'name': 'Max', 'age': 18, 'expr': 2,}, ignore_index=True)) # добавить новую строку 'Max' в самый низ 
# print(df['name']) # Вывести на экран данные по ключу 'name'. Name: name, dtype: object
# print(df.loc['Bill']) # Вывести на экран данные по ключу 'Bill'. Name: Bill, dtype: object

# Другой вариант добавить новую строку 'Max' в самый низ без метода .append. Рабоает, если количество
# передаваемых данных в списке равно количеству столбцов в DataFrame.
# df.loc['Max'] = ['Max', 18, 2]
# print(df)

# df.loc['Sam', 'name'] = 'Sam2' # смнить у 'Sam' 'name' на значение 'Sam2'
# print(df)

# #####################################################################################################
# # ФОРМАТ .CSV
# # coma separate values, сокращенно csv позволяет хранить табличные данные

# # метод .read_csv() считывает данные из таблицы (файла .csv) и записывает данные в переменную
# x = pd.read_csv('WeightLoss.csv')
# # print(x) # можно сразу вывести на печать, не обрабатывая DataFrame()
# df2 = pd.DataFrame(x) # передаем в DataFrame значения переменной x
# # print(df2) # Печатаем результат аналогичный print(x)

# # df2 = df2.fillna(0)  # заменить все NaN на 0
# # print(df2)
# # print(df2.head(2)) # выводит на экран 2 первые строки DataFrame
# # print(df2.head()) # метод .head() по умолчанию показывает первые 5 строк (0, 1, 2, 3, 4)
# # print(df2.tail(2)) # выводит на экран 2 последние строки.
# # print(df2.tail()) # метод .tail() по умолчанию показывает последние 5 строк (33, 32, 31, 30, 29)

# # добавить столбец 'total', значения которого равны сумме трех столбцов 
# df2['total'] = df2['w1'] + df2['w2'] + df2['w3']
# # print(df2) # получаем результат суммы значений трех столбцов
# # # print(df2['total']) # выводит на экран столбец с суммой трех столбцов

# # добавить столбец 'total_gr', значения которого переведены из кг в граммы (*1000)
# df2['total_gr'] = df2['total'] * 1000
# # print(df2) # вывести на экран результат

# # ВЫЧИСЛЕНИЕ ДАННЫХ ПРИ ПОМОЩИ БИБЛИОТЕКИ Numpy

# # при помощи библиотеки numpy к столбцу 'total_gr' применено взятие логорифма и -8
# # print(df2['total_gr'].apply(np.log) - 8)

# # создание новой таблицы. Строки ВСЕ (:), интервал столбцов с w1 по w3
# df3 = df2.loc[:, 'w1':'w3']
# # print(df3)

# # при помощи библиотеки numpy применена функция 'mean' (среднее значение), значения сохранены в столбец
# # и добавлены к таблице df3
# # df3['mean'] = df3.apply(np.mean, axis=1)
# # print(df3)

# # при помощи библиотеки numpy применена функция 'mean' (среднее значение), значения сохранены в столбец
# # и добавлены к таблице df2
# # df2['mean'] = df3.apply(np.mean, axis=1)
# # print(df2)

# # добавление столбца 'max-min' к таблице df2
# f1 = lambda x: x.max() - x.min() # лямбда функция выдает в x результат разности из максимума и минумума
# df2['max-min'] = df3.apply(f1, axis=1)
# # print(df2)

# # ГРУППИРОВКА и СОРТИРОВКА ДАННЫХ
# # Первый элемент списка - ВСЕ из Control, 2ой - ВСЕ из Diet, 3ий - ВСЕ из DietEx.
# # print(list(df2.groupby('group'))) # для отображения на экран приведено к типу списка

# # создан новый DataFrame с данными среднего значения. Применена группировка, затем агрегирование 
# # (применить действие к столбцам групп).
# gr1 = df2.groupby('group').agg('mean')
# # print(gr1['total']) # вывод на экран полученных при помощи агрегирования данных

# # создан новый DataFrame с данными min, средним значением и max. Применена группировка, затем агрегирование
# # (применить действие к столбцам групп).
# gr2 = df2.groupby('group').agg(['min', 'mean', 'max'])
# # print(gr2['total']) # вывод на экран полученных при помощи агрегирования данных

# # сортировка (возрастающая последовательность) по столбцу 'total'
# # print(df2.sort_values('total'))

# # применена сортировка сначалапо 'total', затем по 'id' (передено, в виде списка), ascending=False - по
# # УБЫВАНИЮ
# # print(df2.sort_values(['total', 'id'], ascending=False))

# # print(df2.isnull()) # показать максу отсутствующих данных (с данными NaN)

# # df2 = df2.fillna(0) # метод .fillna() заполнить пустые элементы. Заменить все NaN на 0

# # Удалить строки с отсутствующими данными (с данными NaN). Если вывести первые 10 строк таблицы,
# # применить удаление и сравнить, то видно, что программа удаляет строку с данными NaN.
# # print(df2.head(10))
# # df2 = df2.dropna()
# # print(df2.head(10))

# # print(df2.sort_index()) # сортировка по индексу

# # применена сортировка сначала по 'total', затем по 'id' (передено, в виде списка, ascending=True -
# # по ВОЗРАСТАНИЮ
# # print(df2.sort_values(['total', 'id'], ascending=True))

# # СОХРАНЕНИЕ DataFrame в ФАЙЛ .CSV
# # df2.to_csv('name.csv') # сохранение значений df2 в новый файл 'name.csv'

# # новый DataFrame со столбцами 'id' и 'total'
# df4 = df2[['id', 'total']]
# # print(df4)

# # метод .concat() объединяет таблицы (принимает список из DataFrame). Если DataFrame отличаются по
# # размеру, то недостающие ячейки заполняются значением NaN
# # print(df)
# # print(pd.concat([df4, df]))

# ########################################################################################################

# Проблема форматирования дат (если даты в разных форматах 'дд,мм,гг' или 'гг,мм,дд' или ещё как-то иначе).
df_new1 = pd.read_csv('Dates.csv') # изначально даты в формате 01/01/2012
# print(df_new1)
df_new2 = pd.read_csv('Dates.csv', parse_dates=['Date']) # даты преобразованы к формату 2012-01-01
# print(df_new2)
df_new3 = pd.read_csv('Dates.csv', parse_dates=['Date'], dayfirst=False) # день НЕ первый относительно месяца dayfirst=False
# print(df_new3)
# print(df_new3['Date'].dt.day) # выводим только дни
# print(df_new3['Date'].dt.day_name()) # выводим день недели
df_new3['day_name'] = df_new3['Date'].dt.day_name() # добавим в DataFrame новую колонку 'day_name'
# print(df_new3)

# По умолчанию sep=','. Для корректной работы файла 'Dates2.csv' указать значение sep=';'
df2_new = pd.read_csv('Dates2.csv', sep=';')
print(df2_new)

# СОХРАНЕНИЕ DataFrame в ФАЙЛ .CSV
# # df2_new.to_csv('name2.csv', sep='#') # сохранение значений df2 в новый файл 'name2.csv', разделитель sep='#'
