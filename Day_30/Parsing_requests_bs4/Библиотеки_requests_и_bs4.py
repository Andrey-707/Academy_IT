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

########################################### ДОПОЛНИТЕЛЬНО ############################################

# Файл с HTML кодом сайта
file = 'Parsing_1.txt'

with open(file) as f:
    src = f.read()
soup = BeautifulSoup(src, 'html.parser')

# используем связку методов .find().find()
user_name = soup.find("div", class_="user__name").find("span")
print(user_name.text)

# передача словаря key : value
user_name = soup.find("div", {"class": "user__name"}).find("span")
print(user_name.text)

# передача дополнительного параметра в виде "id"
# программа выдаст ошибку AttributeValue, если тега с атрибутом "aaa" не существует
user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span")
print(user_name.text)

# с помощью метода find_all() соберем все span теги из блока с классом info
find_all_spans_in_user_info = soup.find("div", class_="user__info").find_all("span") 
print(find_all_spans_in_user_info)

# применим цикл к списку и напечатаем содержимое каждого тега span
for item in find_all_spans_in_user_info:
    print(item.text)

# т.к. find_all_spans_in_user_info является списком, можем обращаться к его элементам по индексу
print(find_all_spans_in_user_info[0])

# применяем метод .text
print(find_all_spans_in_user_info[0].text)

# спарсим ссылки на страницы с соц сетями пользователя
social_links = soup.find(class_="social__networks").find("ul").find_all("a")
print(social_links)

# напечатаем ссылки на страницы с соц сетями пользователя поочередно с помощью цекла for
for item in social_links:
    print(item.text)
    print(item)

# ссылки на страницы с соц сетями пользователя можно забрать одной стокой
all_a = soup.find_all("a")
print(all_a)

# применим цикл for к списку с сылками
# ссылка ВСЕГДА ХРАНИТСЯ в атрибуте href. Применим метод .get() и забенем её.
for item in all_a:
    # Применим метод .get()
    item_url = item.get("href")
    print(item_url)

# применим метод .text для более красивого вида содержимого на экране
for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")

# для перемещения по дом-дереву используем методы .find_parent() и .find_parents()
# позволяет перемещаться по коду снизу вверх, а не опускаться вглубь кода
post_div = soup.find(class_="post__text").find_parent()
# забираем блок не целиком, а до первого родителя <div class="user__post__info">
print(post_div)

# в метод .find_parent() можем передавать параметры поиска
# если не укажем ни чего, то получим первого попавшегося родителя, как в примере выше
# если укажем второго родителя, то получим его
post_div = soup.find(class_="post__text").find_parent("div", "user__post")
print(post_div)

# метод find_parents поднимаеся по иерархии до самого верха, включая body и html teg
post_divs = soup.find(class_="post__text").find_parents()
print(post_divs)

# методу .find_parents можно ставить ограничения или фильтры на поиск 
post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
print(post_divs)

# методы .next_element() и .previous_element() двигаются пошагово и возвращают следующий или предыдущий
# элементы в коде

# метод .next_element() работает сверху вниз
# метод .previous_element() работает снизу ввех
next_el = soup.find(class_="post__title").next_element
print(next_el) # в данном случае пограмма выдает пустоту, поскольку .next_element() являтеся перевод строки

# для правильной работы программы используем повторно .next_element()
next_el = soup.find(class_="post__title").next_element.next_element
# вызываем метод .text, чтобы спарсить содержимое
print(next_el.text)

# методы .find_next_sibling() и .find_previous_sibling() возвращают следующий или предыдущий элементы
# внутри искомого тэга

# метод .find_next_sibling()
next_sib = soup.find(class_="post__title").find_next_sibling()
print(next_sib)

# Все методы можно комбинировать между собой
post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
print(post_title)

# получим ссылки с помощью метода .find_all()
links = soup.find(class_="some__links").find_all("a")
print(links)

# С помощью цикла for спарсим атрибуты "attr" из тегов, используя метод .get()
for link in links:
    lik_href_attr_1 = link.get("href")
    link_data_attr_1 = link.get("data-attr")
    print(lik_href_attr_1)
    print(link_data_attr_1)

# С помощью цикла for спарсим атрибуты "attr" из тегов, используя синтаксис в коде
for link in links:
    lik_href_attr_2 = link["href"]
    link_data_attr_2 = link["data-attr"]
    print(lik_href_attr_2)
    print(link_data_attr_2)

# Попробуем найти ссылку, которая начинется на "Одежда"
# получаем None, поскольку BeautifulSoup осуществляет поиск по полному содержанию
find_a_by_text_1 = soup.find("a", text="Одежда")
print(find_a_by_text_1)

# Попробуем другой вариант, чтобы не получить None, как в случае выше
find_a_by_text_2 = soup.find("a", text="Одежда для взрослых")
print(find_a_by_text_2)

# Исправим код, чтобы не получить None, как в предыдущий раз для этого импортируем модуль re
import re

find_a_by_text_3 = soup.find("a", text=re.compile("Одежда"))
print(find_a_by_text_3)

# Найдем все ссылки, которые содержат текст "Одежда" или "одежда"
find_all_clothes = soup.find_all(text=re.compile("[Оо]дежда"))
print(find_all_clothes)
