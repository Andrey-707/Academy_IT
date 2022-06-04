# Вам дан файл-шаблон с неизвестным содержимым и неизвестным количеством строк. А так же файл с почтами,
# именами и фамилиями.

# Необходимо написать алгоритм, который будет создавать новые файлы на основе шаблона. В новом файле
# на первой строе должна быть указана почтаадресата, а на последней - номер файла в формате
# <<номер_текущего/колечество_всех>>. Где-то по центру необходимо вставить Фамилию и Имя адресата.
# Для сгенерированных файлов создайте отдельную директорию.

'''
Пример файла с именами (файл personal_data.txt):

BreakInvention@gmail.com Калинин Кирилл
MemoryUniverse@yandex.ru Зимина Амина
SealSidewalk@mail.ru Уткина Анна
MineBrokenFire@gmail.com Андреев Никита
ThemeLibraryAlpha@mail.ru Смирнов Владимир
ReconSlice@yandex.ru Ефимов Мирослав
CircleForceNear@gmail.com Воронин Вадим
ProducePaymentBloxxer Морозова Софья
GermNotebookCool@mail.ru Казакова Виктория
YarnZero@yandex.ru Зимина Анастасия

Пример файла-шаблона 1 (файл message_template_1.txt):

<почта>
Здравствуйте, <ФИ>!
Вы приглашены на мероприятие!
Мероприятие состоится в 18:00.
<номер>

Пример сгенерированного письма 1:

BreakInvention@gmail.com
Здравствуйте, Калинин Кирилл!
Вы приглашены на мероприятие!
Мероприятие состоится в 18:00.
1/10

Пример файла-шаблона 2 (файл message_template_2.txt)

<почта>

Уважаемый(ая) <ФИ>!

Благодарим Вас за плодотворное сотрудничество и вклад в развитие нашей компании.
Приглашаем Вас на новогодний вечер, который мы устраиваем в честь наших партнеров, сотрудников и друзей.

В преддверии Нового 2021 года мы соберемся вместе, чтобы приятно провести время в праздничной атмосфере
и пожелать друг другу успехов и новых побед.

Пусть наступающий год принесет Вам только приятные перемены, каждый день будет успешным в личной жизни
и плодотворным в работе!

Ждём вас 30 декабря в 104 аудитории в 17:00.

<номер>


Пример сгенерированного письма 2:

SealSidewalk@mail.ru

Уважаемый(ая) Уткина Анна!

Благодарим Вас за плодотворное сотрудничество и вклад в развитие нашей компании.
Приглашаем Вас на новогодний вечер, который мы устраиваем в честь наших партнеров, сотрудников и друзей.

В преддверии Нового 2021 года мы соберемся вместе, чтобы приятно провести время в праздничной атмосфере
и пожелать друг другу успехов и новых побед.

Пусть наступающий год принесет Вам только приятные перемены, каждый день будет успешным в личной жизни
и плодотворным в работе!

Ждём вас 30 декабря в 104 аудитории в 17:00.

3/10

'''
from rich import print


# Решение_1.
# ПРОГРАММА СОЗДАЕТ 10 ПИСЕМ ДЛЯ ВСЕХ 10 УЧАСТНИКОВ РАССЫЛКИ ПО ТЕКСТУ ШАБЛОНА message_template_1.txt

# получить данные из файла "personal_data.txt" в виде списка из строк
personal_data = []
with open("personal_data.txt", encoding="utf-8") as r:
    for line in r.readlines():
        personal_data.append(line)
    # personal_data = f.read().split("\n") # создание списка без итераций по строками
# print(personal_data)

'''OUT: 
[
    '\ufeffBreakInvention@gmail.com Калинин Кирилл\n',
    'MemoryUniverse@yandex.ru Зимина Амина\n',
    'SealSidewalk@mail.ru Уткина Анна\n',
    'MineBrokenFire@gmail.com Андреев Никита\n',
    'ThemeLibraryAlpha@mail.ru Смирнов Владимир\n',
    'ReconSlice@yandex.ru Ефимов Мирослав\n',
    'CircleForceNear@gmail.com Воронин Вадим\n',
    'ProducePaymentBloxxer Морозова Софья\n',
    'GermNotebookCool@mail.ru Казакова Виктория\n',
    'YarnZero@yandex.ru Зимина Анастасия\n'
]
'''

# получить данные из файла "message_template_1.txt" в виде текста
with open("message_template_1.txt", encoding="utf-8") as r:
    message = r.read()
# print(message)

'''OUT:
<почта>
Здравствуйте, <ФИ>!
Вы приглашены на мероприятие!
Мероприятие состоится в 18:00.
<номер>
'''

# # создать файлы для каждого участника рассылки и заполнить их сообщениями
# for i, row in enumerate(personal_data):
#     m = message # данные в переменной 'm' обновляется на текст шаблона каждую итерацию
    
#     mail, sec_name, name = row[:-1].split(" ") # если при создании personal_data не избавились от символа перевода строки
#     number = str(i+1) + "/" + str(len(personal_data))

#     m = m.replace("<почта>", mail)
#     m = m.replace("<ФИ>", sec_name + " " + name)
#     m = m.replace("<номер>", number)

#     f = open(f"New_Dir\\1-{i+1}.txt", "w", encoding="utf-8")
#     f.write(m)
#     f.close()

# или так с проверками на ошибки:
for i, row in enumerate(personal_data):
    m = message # данные в переменной 'm' обновляется на текст шаблона каждую итерацию

    try:
        mail, sec_name, name = row[:-1].split(" ") # если при создании personal_data не избавились от символа перевода строки
        number = f"{i+1}/{len(personal_data)}"
    except ValueError:
        print("ValueError! Ошибка при создании mail, sec_name, name, number.")
        mail, sec_name, name, number = "unknown_mail", "unknown_sec_name", "unknown_name", "unknown_number"
    finally:
        print(f"Create message {number}.")

    m = m.replace("<почта>", mail)
    m = m.replace("<ФИ>", sec_name + " " + name)
    m = m.replace("<номер>", number)

    try:
        with open("New_Dir\\1-" + str(i+1) + ".txt", "w", encoding="utf-8") as f:
            f.write(m)
    except FileNotFoundError:
        print("[red]FileNotFoundError! Этой папки не существует![/]")
        f.close()


##################################################################################################################

# Решение_2.
# ПРОГРАММА СОЗДАЕТ 10 ПИСЕМ ДЛЯ ВСЕХ 10 УЧАСТНИКОВ РАССЫЛКИ ПО ТЕКСТУ ШАБЛОНА message_template_2.txt

# получить данные из файла "personal_data.txt" в виде списка из строк
with open("personal_data.txt", "r", encoding="utf8") as f:
    personal_data = f.read().split("\n")[:-1]
# print(personal_data)

'''OUT: 
[
    '\ufeffBreakInvention@gmail.com Калинин Кирилл',
    'MemoryUniverse@yandex.ru Зимина Амина',
    'SealSidewalk@mail.ru Уткина Анна',
    'MineBrokenFire@gmail.com Андреев Никита',
    'ThemeLibraryAlpha@mail.ru Смирнов Владимир',
    'ReconSlice@yandex.ru Ефимов Мирослав',
    'CircleForceNear@gmail.com Воронин Вадим',
    'ProducePaymentBloxxer Морозова Софья',
    'GermNotebookCool@mail.ru Казакова Виктория',
    'YarnZero@yandex.ru Зимина Анастасия'
]
'''

# получить данные из файла "message_template_2.txt" в виде текста
with open("message_template_2.txt", "r", encoding="utf8") as f:
    message = f.read()
# print(message)

'''OUT: 
<почта>

Уважаемый(ая) <ФИ>!

Благодарим Вас за плодотворное сотрудничество и вклад в развитие нашей компании.
Приглашаем Вас на новогодний вечер, который мы устраиваем в честь наших партнеров,
сотрудников и друзей.

В преддверии Нового 2021 года мы соберемся вместе, чтобы приятно провести время в
праздничной атмосфере
и пожелать друг другу успехов и новых побед.

Пусть наступающий год принесет Вам только приятные перемены, каждый день будет успешным в личной жизни
и плодотворным в работе!

Ждём вас 30 декабря в 104 аудитории в 17:00.

<номер>
'''

# создать файлы для каждого участника рассылки и заполнить их сообщениями
for i, row in enumerate(personal_data):
    m = message
    try:
        mail, sec_name, name = row.split(" ")
        number = str(i+1) + "/" + str(len(personal_data))
    except ValueError:
        print("ValueError! Ошибка при создании mail, sec_name, name, number.")
        mail, sec_name, name, number = "unknown_mail", "unknown_sec_name", "unknown_name", "unknown_number"
    finally:
        print(f"Create message {number}.")

    m = m.replace("<почта>", mail)
    m = m.replace("<ФИ>", sec_name + " " + name)
    m = m.replace("<номер>", number)

    try:
        with open("New_Dir\\1_" + str(i+1) + ".txt", "w", encoding="utf-8") as f:
            f.write(m)
    except FileNotFoundError:
        print("[red]FileNotFoundError! Этой папки не существует![/]")
        f.close()


##################################################################################################################

# # Решение_3.
# # ПРОГРАММА СОЗДАЕТ 1 ПИСЬМО ДЛЯ ПЕРВОГО УЧАСТНИКА РАССЫЛКИ ПО ТЕКСТУ ШАБЛОНА message_template_1.txt

# # В этом решении присутствует множество различных манипуляций с данными файла шиблона сообщения и файла с
# # персональными данными. Для данного случая эти манипуляции излишни. Оставил решение на тот случай,
# # если возникнет необходимость всячески "поиграться" с тестом, например, удалить из текста символ кодировки
# # (\ufeff), проставить дополнительные знаки препинания, переводы строк (\n), добавить в строки дополнительный
# # текст и прочее. 

# # получить данные из файла "personal_data.txt" в виде списка из строк
# personal_data_l = []
# with open("personal_data.txt", encoding="utf-8") as r:
#     for line in r.readlines():
#         personal_data_l.append(line)

# # print(personal_data_l)

# '''OUT: 
# [
#     '\ufeffBreakInvention@gmail.com Калинин Кирилл\n',
#     'MemoryUniverse@yandex.ru Зимина Амина\n',
#     'SealSidewalk@mail.ru Уткина Анна\n',
#     'MineBrokenFire@gmail.com Андреев Никита\n',
#     'ThemeLibraryAlpha@mail.ru Смирнов Владимир\n',
#     'ReconSlice@yandex.ru Ефимов Мирослав\n',
#     'CircleForceNear@gmail.com Воронин Вадим\n',
#     'ProducePaymentBloxxer Морозова Софья\n',
#     'GermNotebookCool@mail.ru Казакова Виктория\n',
#     'YarnZero@yandex.ru Зимина Анастасия\n'
# ]
# '''

# # преобразовать список в текст
# personal_data_s  = "".join(personal_data_l)
# # print(personal_data_s)

# '''OUT:
#  ﻿BreakInvention@gmail.com Калинин Кирилл
# MemoryUniverse@yandex.ru Зимина Амина
# SealSidewalk@mail.ru Уткина Анна
# MineBrokenFire@gmail.com Андреев Никита
# ThemeLibraryAlpha@mail.ru Смирнов Владимир
# ReconSlice@yandex.ru Ефимов Мирослав
# CircleForceNear@gmail.com Воронин Вадим
# ProducePaymentBloxxer Морозова Софья
# GermNotebookCool@mail.ru Казакова Виктория
# YarnZero@yandex.ru Зимина Анастасия
# '''

# # получить данные из файла "message_template_1.txt" в виде списка из строк
# message_template_l = []
# with open("message_template_1.txt", encoding="utf-8") as r:
#     for line in r.readlines():
#         message_template_l.append(line)

# # print(message_template_l)

# '''OUT:
# [
#     '<почта>\n',
#     'Здравствуйте, <ФИ>!\n',
#     'Вы приглашены на мероприятие!\n',
#     'Мероприятие состоится в 18:00.\n',
#     '<номер>\n'
# ]
# '''

# # преобразовать список в текст
# message_template_s  = "".join(message_template_l)
# # print(message_template_s)

# '''OUT:
# <почта>
# Здравствуйте, <ФИ>!
# Вы приглашены на мероприятие!
# Мероприятие состоится в 18:00.
# <номер>
# '''

# # разбить такст personal_data_s на отдельные составляющие (элементы списка ОТДЕЛЬНО ПОЧТА, ФАМИЛИЯ И ИМЯ)
# # изначальный список personal_data_l состоит из ГОТОВЫХ СТРОК
# mail_secname_name = personal_data_s.split()
# # print(mail_secname_name)

# '''OUT:
# [
#     '\ufeffBreakInvention@gmail.com',
#     'Калинин',
#     'Кирилл',
#     'MemoryUniverse@yandex.ru',
#     'Зимина',
#     'Амина',
#     'SealSidewalk@mail.ru',
#     'Уткина',
#     'Анна',
#     'MineBrokenFire@gmail.com',
#     'Андреев',
#     'Никита',
#     'ThemeLibraryAlpha@mail.ru',
#     'Смирнов',
#     'Владимир',
#     'ReconSlice@yandex.ru',
#     'Ефимов',
#     'Мирослав',
#     'CircleForceNear@gmail.com',
#     'Воронин',
#     'Вадим',
#     'ProducePaymentBloxxer',
#     'Морозова',
#     'Софья',
#     'GermNotebookCool@mail.ru',
#     'Казакова',
#     'Виктория',
#     'YarnZero@yandex.ru',
#     'Зимина',
#     'Анастасия'
# ]
# '''

# # Используя метод 'list comprehension' создадим список с <ФИ>
# persons = [list(mail_secname_name[i+1:i+3]) for i in range(0, len(mail_secname_name), 3)]
# # print(persons)

# '''OUT:
# [
#     ['Калинин', 'Кирилл'],
#     ['Зимина', 'Амина'],
#     ['Уткина', 'Анна'],
#     ['Андреев', 'Никита'],
#     ['Смирнов', 'Владимир'],
#     ['Ефимов', 'Мирослав'],
#     ['Воронин', 'Вадим'],
#     ['Морозова', 'Софья'],
#     ['Казакова', 'Виктория'],
#     ['Зимина', 'Анастасия']
# ]     
# '''

# # Используя метод 'list comprehension' создадим список с почтами
# mails = [mail_secname_name[i:i+1] for i in range(0, len(mail_secname_name), 3)]
# # print(mails)

# '''OUT:
# [
#     ['\ufeffBreakInvention@gmail.com'],
#     ['MemoryUniverse@yandex.ru'],
#     ['SealSidewalk@mail.ru'],
#     ['MineBrokenFire@gmail.com'],
#     ['ThemeLibraryAlpha@mail.ru'],
#     ['ReconSlice@yandex.ru'],
#     ['CircleForceNear@gmail.com'],
#     ['ProducePaymentBloxxer'],
#     ['GermNotebookCool@mail.ru'],
#     ['YarnZero@yandex.ru']
# ]
# '''

# # разбить такст message_template_s на отдельные составляющие (элементы списка ОТДЕЛЬНО КАЖДОЕ СЛОВО)
# # изначальный список message_template_s состоит из ГОТОВЫХ СТРОК
# message_template_edited = message_template_s.split() 
# # print(message_template_edited)

# '''OUT:
# [
#     '<почта>',
#     'Здравствуйте,',
#     '<ФИ>!',
#     'Вы',
#     'приглашены',
#     'на',
#     'мероприятие!',
#     'Мероприятие',
#     'состоится',
#     'в',
#     '18:00.',
#     '<номер>'
# ]
# '''

# # отредактировать список message_template_edited (удалить симол кодировки, зашитый в начале списка с почтами, заменить
# # "<почта>", "<ФИ>!", "<номер>" на почту, ФИ и порядковый номер усастника рассылки)
# for i, j in enumerate(message_template_edited):
#     if "<почта>" in j:
#         message_template_edited[i] = "".join(mails[0])[1:] # НЕ СНАЧАЛА, ПОТОМУ ЧТО В НАЧАЛЕ ЗАШИТ СИМВОЛ КОДИРОВКИ (\ufeff)
#     elif "<ФИ>!" in j:
#         message_template_edited[i] = " ".join(persons[0])+"!" # И ДОБАВИТЬ ВОСКЛИЦАТЕЛЬНЫЙ ЗНАК
#     elif "<номер>" in j:
#         message_template_edited[i] = "1/{}".format(len(mails)) # ПОРЯДКОВЫЙ НОМЕР УЧАСТНИКА РАССЫЛКИ 1/длина списка участников
# # print(message_template_edited)

# '''OUT:
# [
#     'BreakInvention@gmail.com',
#     'Здравствуйте,',
#     'Калинин Кирилл!',
#     'Вы',
#     'приглашены',
#     'на',
#     'мероприятие!',
#     'Мероприятие',
#     'состоится',
#     'в',
#     '18:00.',
#     '1/10'
# ]
# '''

# # преобразовать отредактированный список message_template_edited в текст
# result = " ".join(message_template_edited)
# # print(result)

# '''OUT:
# BreakInvention@gmail.com Здравствуйте, Калинин Кирилл! Вы приглашены на мероприятие! Мероприятие состоится в 18:00. 1/10
# '''

# # отредактировать текст, расставить символы перевода строки в необходимые места
# # при помощи метода строки "".find() опредить по какому индексу поставить перевод строки
# # print(result.find("Здр")) # индекс символа - 25
# result = result[:25] + "\n" + result[25:]
# # print(result.find("Вы")) # индекс символа - 56
# result = result[:56] + "\n" + result[56:]
# # print(result.find("Мер")) # индекс символа - 87
# result = result[:87] + "\n" + result[87:]
# # print(result.find("1/10")) # индекс символа - 119
# result = result[:119] + "\n" + result[119:]
# # print(result)

# '''OUT:
# BreakInvention@gmail.com
# Здравствуйте, Калинин Кирилл!
# Вы приглашены на мероприятие!
# Мероприятие состоится в 18:00.
# 1/10
# '''

# # создаем файл и заполнить его текстовыми данными из переменной result
# with open("1-10.txt", mode="w", encoding="utf-8") as w:
#     w.write(result)

# # открываем файл на чтение
# with open("1-10.txt", encoding="utf-8") as r:
#     print(r.read())

# '''OUT:
# BreakInvention@gmail.com
# Здравствуйте, Калинин Кирилл!
# Вы приглашены на мероприятие!
# Мероприятие состоится в 18:00.
# 1/10
# '''
