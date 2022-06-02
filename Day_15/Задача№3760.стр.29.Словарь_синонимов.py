# Задача№3760.стр.29.Словарь синонимов.
# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для одного данного слова определите его синоним.

# Входные данные:
# Программа получает на входе количество пар синонимов N, далее следует N строк, каждая строка содержит ровно два
# слова-синонима. После этого следует одно слово.
# Выходные данные:
# Программа должна вывести синоним к данному слову.

# Примечание.
# Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но решение с использованием словаря проще.

# Пример.
# Входные данные:
# 3 
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# Выходные данные:
# Bye

# Решение.
from rich import print


n = 4 # переменная используется при генерации словаря через input()

# введем переменные в виде строк и с помощью них создадим словарь
s1 = "дерево ель"
s2 = "камень янтарь"
s3 = "металл золото"
s4 = "вода сок"

# создание словаря из строк при вводе от пользователя, т.е через input():
#some_dict = dict(input("Введите через пробелы 'слово синоним':\n").split(' ') for i in range(n))

# или если данные записаны в переменные s1, s2, s3 и s4:
# Функция dict() является конвертирующей функцией, т.е. создает словарь из списков
some_dict = dict(i.split(" ") for i in (s1, s2, s3, s4))
print(some_dict)

# вывод значения по ключу
print("[bold magenta]Вывод значения по ключу[/]")
print("value:", some_dict[input("key: ")])
# или так
print("[bold magenta]Вывод значения по ключу[/]")
print("value:", some_dict.get(input("key: ")))

# вывод ключа по значению
print("[bold magenta]Вывод ключа по значению[/]")
value = input("value: ")
for k, v in some_dict.items():
    if v == value: 
        print("key:", k)

# либо можно сделать инверсию key-value = value-key циклом
# reverse_dict = {}
# for k, v in some_dict.items():
#     reverse_dict[v] = k

# или можно воспользоваться генератором словаря и перевернуть key-value = value-key в одну строчку 
reverse_dict = {v: k for k, v in some_dict.items()}

# и выводить значение из словаря some_dict по ключу словаря some_dict (или значению словаря new_dict)
print("[bold magenta]Вывод ключа по значению[/]")
print("key:", reverse_dict[input("value: ")])
# или так
print("[bold magenta]Вывод ключа по значению[/]")
print("key:", reverse_dict.get(input("value: ")))


######################################################################################################
# Решение_2. Ручной ввод. Программа выведет что будет ключем в текущем словаре, а что значением key= : value=

N = int(input("Кол-во пар в словаре: "))

some_dict = dict()
for i in range(N):
    s = tuple(input("Введите через пару слов:\n").split()) # дерево ель
    d = dict([s])
    some_dict.update(d)
    print(some_dict)


for i, n in some_dict.items():
    if i == s:
        a = n
        print(f"[yellow]Dict Items[/]:\nkey={s}: value={a}")
    elif n == s:
        a = i
        print(f"[yellow]Dict Items[/]:\nkey={a}: value={s}")
    else:
        print("Не найдено")


######################################################################################################
# Решение_3. Решение аналогичное решению_2, но добавлена функция с переменным числом аргументов.
def synonyms(**kwargs):
    global s
    for i in kwargs:
        # если value слвоаря == s - выводи key
        if i == s:
            return kwargs[i]
        # иначе если key слвоаря == s - выводи value
        elif kwargs[i] == s:
            return i

N = int(input("Кол-во пар в словаре: "))
some_dict = dict()

# N итераций цикла for
for t in range(int(N)):
    l = (input("Введите через пару слов:\n")).split() # дерево ель
    some_dict[l[0]] = l[1]

# поиск слова по синониму (global s)
s = input("Введите слово: ")

# в функцию передается словарь
for k, v in some_dict.items():
    if s == k:
        print(f"[yellow]Dict Items[/]:\nkey={s}: value={synonyms(**some_dict)}")
    elif s == v:
        print(f"[yellow]Dict Items[/]:\nkey={synonyms(**some_dict)}: value={s}")
    else:
        print("Не найдено")
