# JSON (eng. JavaScript Object Notation) - это формат хранения данных в виде списков и словарей,
# поддерживающий произвольную вложенность

# Код для JavaScript
# var cat = {
#     name: 'Barsik',
#     age: 7
# }

# Пример вложенности json файлов на примере обычного словаря Python
dic_json = {
    'name': 'Barsik',
    'age': 7,
    'maels': ['w1', 'w2'],
    'mother': {
        'name': 'Olga',
        'age': 10,
    }
}
# OUT: {'name': 'Barsik', 'age': 7, 'maels': ['w1', 'w2'], 'mother': {'name': 'Olga', 'age': 10}}
# print(type(dic_json), dic_json) # <class 'dict'>

import json

json1 = json.dumps(dic_json)  # dumps = dump + string - для данных в формате str
# OUT: {"name": "Barsik", "age": 7, "maels": ["w1", "w2"], "mother": {"name": "Olga", "age": 10}} # кавычки отличаются!!!
# print(type(json1), json1) # <class 'str'>

list_json = ["Bars", 1, 3, 6, "Oranges"]
json2 = json.dumps(list_json)
# OUT: ["Bars", 1, 3, 6, "Oranges"]
# print(type(json2), json2) # <class 'str'>

# OUT: false
# print(json.dumps(False))

# Сохранить в файл 'name.json' (файл можно открыть в блокноте)
# with open('name.json', 'w') as file:
#     json.dump(dic_json, file) # метод .dump() - если нужно json сохранить в файл

# Прочесть файл 'name.json'
# with open('name.json', 'r') as file:
#     json_load = json.load(file) # метод .load() - для загрузки файла
#     print(json_load) # {'name': 'Barsik', 'age': 7, 'maels': ['w1', 'w2'], 'mother': {'name': 'Olga', 'age': 10}}
#     print(type(json_load)) # <class 'dict'>

str_json = """
{
    "name": "Barsik",
    "age": 7,
    "maels": ["w1", "w2"],
    "mother": {
        "name1": "Olga",
        "age1": 10
    }
}
"""
json3 = json.loads(str_json) # loads = load + string - для перевода str в json
# OUT: <class 'dict'> {'name': 'Barsik', 'age': 7, 'maels': ['w1', 'w2'], 'mother': {'name1': 'Olga', 'age1': 10}}
# print(type(json3), json3)

import pandas as pd

dat = pd.read_json("https://api.github.com/users")
# print(type(dat)) # <class 'pandas.core.frame.DataFrame'>
# print(dat.info()) # информация по DataFrame
# print(dat) # выводит DataFrame на экран
# dat.to_csv('json.csv') # сохранить json в файл формата .csv

with open('name.json', 'r') as f:
    data = json.load(f)
# OUT: {'name': 'Barsik', 'age': 7, 'maels': ['w1', 'w2'], 'mother': {'name': 'Olga', 'age': 10}}
# print(data)

# не работает
# df_data = pd.read_json('name.json')
# print(df_data) # ValueError: Mixing dicts with non-Series may lead to ambiguous ordering.

# ЕСЛИ ДАННЫЕ ВНУТРИ ФАЙЛА 'name.json' ВЗЯТЬ В КВАДРАТНЫЕ СКОБКИ, ТО РАБОТАЕТ!!!
df_data = pd.read_json('name2.json')
# print(df_data)

# Добавим внутри файла ещё одного кота по имени 'Tom'
df_data = pd.read_json('name3.json')
# print(df_data)

# Сохранить DataFrame в файл формата .csv
# df_data.to_csv('name3.csv')

# Все три файла открываются корректно, последние два - тип данных <class 'list'>
# with open('name.json', 'r') as file:
#     json_load = json.load(file)  # load - для загрузки файла
#     print(json_load)
#     print(type(json_load))
# with open('name2.json', 'r') as file:
#     json_load = json.load(file)  # load - для загрузки файла
#     print(json_load)
#     print(type(json_load))
with open('name3.json', 'r') as file:
    json_load = json.load(file)  # load - для загрузки файла
#     print(json_load)
#     print(type(json_load))

# OUT: <class 'str'> Barsik
# print(type(json_load[0]['name']), json_load[0]['name']) # обратиться к первому элементу, обратимся по ключу 'name'
# OUT: <class 'int'> 7
# print(type(json_load[0]['age']), json_load[0]['age']) # обратиться к первому элементу, обратимся по ключу 'age'
# OUT: <class 'dict'> {'name': 'Olga', 'age': 10}
# print(type(json_load[0]['mother']), json_load[0]['mother']) # обратиться к первому элементу, обратимся по ключу 'mother'
# print(type(json_load[0]), json_load[0]) # обратиться к первому элементу и напечатать его

# Пример показывает, что можно работать с элементом по индексу 0 как со словарем
# d = {"a": 1}
# print(d.items())
# print(json_load[0].items())



"""Попробуем прочесть файл json обычным способом:"""
# Данный способ выдает строку
with open('name.json', 'r') as file:
    a = file.read()
# OUT: {"name": "Barsik", "age": 7, "maels": ["w1", "w2"], "mother": {"name": "Olga", "age": 10}} <class 'str'>
print(a, type(a))
# print(list(a)) # переводит строку в список
print(a[0], type(a[0])) # первый элемент строки - фигурная скобка { <class 'str'>
