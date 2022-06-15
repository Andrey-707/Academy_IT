# Модуль_pymysql.Работа_с_СУБД

# Создаем файл с настройками "config", в нем прописаны host, port, user, password, database.
# Из файла импортируем данные конфиги host, port, user, password, database.

# В PHP MyAdmin создаю НОВУЮ пустую БД с именем "day_27", внутри config прописываем database = "day_27"

import pymysql

from config import host, port, user, password, database # импортируем данные конфиги
from rich import print # для визуализации вывода данных на экран импортирую модуль принт

# Чтобы исключить ошибки программы или обработать их, заранее обернем программу в структуру <try-except>
try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    print(f"Подключение к БД '{database}'...")

    # Чтобы выполнить иньекцию в БД нужно создать курсор (поскольку курсор нужно закрывать искользуется
    # конструкция <with as>)
    # cursor = connection.cursor() # ниже создание переменной курсора происходит внутри конструкции <with as>

##################################
## методы, применяемые к cursor ##
##################################

    # метод .execute() выполняет команду, которая передана внутри метода
    # метод .fetchall() передает ответ от SELECT
    # метод .commit() отправляет данные в БД

######################
## добавить таблицу ##
######################

    # Команда создает таблицу `users`, настройки таблицы прописаны внутри скобок ()
    # когда настройки прописаны и скобки закрываются нужно обязательно поставить символ точка с запятой ';'
    with connection.cursor() as cursor:
        create_table = "CREATE TABLE `users` (id INT AUTO_INCREMENT, name VARCHAR(32), " \
                       "password VARCHAR(32), email VARCHAR(32), PRIMARY KEY (id));"
        cursor.execute(create_table)
        print("Таблица `users` создана")
        # после выполнения команды создается новая таблица в БД "day_27"

        # !!! .commit() не нужен при создании и удалении таблицы !!!
        
        # если попытаться запустить команду второй раз, программа выдаст ошибку:
        # (1050, "Table 'users' already exists")

###############################
## заполнить таблицу (AI ON) ##
###############################

    # Заполнение таблицы: INSERT INTO `имя_таблицы` (столбцы) VALUES (значения);

    # Команда вставляет в таблицу `users` новые данные, прописанные в VALUES
    # !!! не сработает, если выключен AUTO_INCREMENT !!!
    with connection.cursor() as cursor:
        insert = "INSERT INTO `users` (name, password, email) VALUES ('Tom6', 'tomqwerty3', 'tombus3@mail.ty');"
        cursor.execute(insert)
        connection.commit()
        print("Данные добавлены")

        # если попытаться запустить команду второй раз, программа добавит такого же самого пользователя и если 
        # в настройках таблицы стоит галочка AUTO_INCREMENT, id будет увеличиваться на 1 с каждым добавление нового
        # (или того же самого при повторном запуске команды) пользователя

        # чтобы ВЫКЛЮЧИТЬ AUTO_INCREMENT:
        # "выбрать_БД" -> "выбрать_ТАБЛИЦУ" -> структура -> изменить id -> убрать галочку под AUTO_INCREMENT

        # если попытаться запустить команду когда выключен AUTO_INCREMENT, программа выдает ошибку:
        # (1364, "Field 'id' doesn't have a default value")

###############################
## удалить данные из таблицы ##
###############################

    # # Команда удалит из таблицы `users` данные, удавлетворяющие условиям, прописанным в WHERE
    # with connection.cursor() as cursor:
    #     delete = "DELETE FROM `users` WHERE name='Tom6';"
    #     cursor.execute(delete)
    #     connection.commit()
    #     print("Данные удалены")

    # # если попытаться запустить команду второй раз, программа ни чего НЕ удилит и НЕ вылетит с ошибкой

################################
## заполнить таблицу (AI OFF) ##
################################

    # # мы удалили пользователя 'Tom6', у которого был id=3, добавим нового пользователя 'Tom' с id=1
    # # помним, что AUTO_INCREMENT отключен, соответственно id прописываем вручную
    # with connection.cursor() as cursor:
    #     insert = "INSERT INTO `users` (id, name, password, email) VALUES (1, 'Tom', 'tomqwerty3', 'tombus3@gmail.com');"
    #     cursor.execute(insert)
    #     connection.commit()
    #     print("Данные добавлены")

    #     # если попытаться запустить команду второй раз, программа НЕ добавит такого же самого пользователя, а
    #     # выдаст ошибку: (1062, "Duplicate entry '1' for key 'PRIMARY'")

###############################
## обновить данные в таблице ##
###############################

    # # Команда обновит (поменяет) данные из таблицы `users`, удавлетворяющие условиям, прописанным в WHERE
    with connection.cursor() as cursor:
        update = "UPDATE `users` SET password = 'TOMqwerty' WHERE id = 1;"
        cursor.execute(update)
        connection.commit()
        print("Данные изменены")

###########################
## вывод данных на экран ##
###########################

    # Команда выводит данные из таблице `users`
    with connection.cursor() as cursor:
        select = "SELECT * FROM `users`"
        cursor.execute(select)
        rows = cursor.fetchall()
        print("Вывод данных на экран:", rows) # программа выдает данные в формате json

######################
## удаление таблицы ##
######################

    # команда удалит (ДРОПНЕТ) таблицу `users` из БД "day_27"
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE `users`")
        print("Таблица `users` удалена")

        # !!! .commit() не нужен при создании и удалении таблицы !!!

except Exception as ex:
    print("Ошибка при подключении к БД:")
    print(ex)
