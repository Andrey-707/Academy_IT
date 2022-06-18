# Библиотеки requests и bs4.
# pip install bs4
# pip install lxml

import requests

from bs4 import BeautifulSoup
from rich import print

# ##################################### Библиотека bs4 #######################################################

# # Чтение данных с помощью библиотеки bs4
# URL1 = "https://lenta.ru/"
# URL2 = "https://ria.ru/"
# r = requests.get(URL1)
# src = r.text
# # Устиновить bs4 и lxml, далее:
# soup = BeautifulSoup(src, "lxml") # "lxml" - парсер
# # print(soup) # программа выдает очень много HTML кода

# # Вывести шапку (title) сайта на экран
# title = soup.title
# # шапка сайта в HTML:              
# print(title) # OUT: <title>Lenta.ru - Новости России и мира сегодня</title>
# # шапка сайта в текстовом формате: 
# print(title.text) # OUT: Lenta.ru - Новости России и мира сегодня

# ################################ Методы .find() и .find_all() библиотеки bs4 ###############################

# # метод .find() выводит первый попавшийся div на сайте
# page_div = soup.find("div")
# print(page_div)

# # Вывести первый div в текстовом формате
# page_div = soup.find("span")
# print(page_div.text) # OUT: Лента добра

# # Метод .find_all() выводит в виде списка ВСЕ div на сайте
# page_div_all = soup.find_all("div")
# print(page_div_all) # выводит ОЧЕНЬ МНОГО текста на экран
# # Можно обратиться к списку по индексу и вывести ОДИН нужный div
# print(page_div_all[2]) # выводит ОЧЕНЬ МНОГО текста на экран

# # Вывести ВСЕ div в текстовом формате
# page_div_all = soup.find_all("span")
# for _ in page_div_all:
#     print(_.text)

# Сменим сайт на tass.ru

# # Чтение данных с помощью библиотеки bs4
URL = "https://tass.ru/"
r = requests.get(URL)
src = r.text
# Устиновить bs4 и lxml, далее:
soup = BeautifulSoup(src, "lxml") # "lxml" - парсер
# print(soup) # выводит ОЧЕНЬ МНОГО текста на экран

# В браузере Настроки -> Доп инструменты -> Инструменты разработчика
# Зайти на сайте в инструментах разработчика найти div и его класс

# Вывести div на экран с помощью метода .findall()
page_div_all = soup.find_all("div")
# print(page_div_all[1]) # если нужно просмотреть отдельно div

# Или так с помощью метода .find()
# Вывести div на экран с помощью метода .find()
class_name = """ds_ext_caption-OrqJe ds_ext_caption--size_default-d79Mb ds_ext_caption--\
font_weight_medium-RPusg ds_ext_caption--color_primary-nxY7t"""
div_ = soup.find("div", class_=class_name)
# print(div_)

# Если классов много, выводятся в виде списка. Вывести все div на экран с помощью метода .find_all().
# divs = soup.find_all("div", class_=class_name)
# print(divs)

# Вывести все div на экран с помощью метода .find_all(). В цикле выводятся все элементы списка
# divs = soup.find_all("div", class_=class_name)
# for i in divs:
#     print(i)

# Вывести текст
# divs = soup.find_all("div", class_=class_name)
# for i in divs:
#     print(i.text)

# Вывести текст первого div
divs = soup.find_all("div", class_=class_name)
# print(divs[0].text)

# # Если внутри div находится другой div (не для данного примера)
# divs = soup.find("div", class_=class_name1).find_all("div", class_=class_name2)
# for i in divs:
#     print(i.text)

# # Метод, аналогичный предыдущему (не для данного примера)
# divs = soup.find_all("div", class_=class_name1)
# for i in divs:
#     # print(i.text)
#     div = i.find_all("div", class_=class_name2)
#     for j in div:
#         print(j.text)

# Метод .find_parent() позволяет подняться выше в дереве каталога
divs = soup.find("div", class_=class_name).find_parent()
for i in divs:
    print(i.text)
