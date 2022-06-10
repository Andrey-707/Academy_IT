# Модуль_os

import os


# тип ОС (nt = windows)
print(os.name)

# словарь с переменными окружения
# print(os.environ)

# доступ к переменной среды temp
print(os.getenv("TMP"))

# папка из которой запускается исполняемый файл
print(os.getcwd())

# изменить текущую папку на ту, что указана. НЕ ЗАПУСКАТЬ!!!
# # print(os.chdir(r"D:\folder"))

# наличие файла
print(os.path.exists("test.py")) # OUT: True

# проверка, является ли это файлом
print(os.path.isfile("test.py")) # OUT: True

# проверка, является ли это папкой
print(os.path.isdir("D:\\Python")) # OUT: True

# создание новой директории
os.mkdir("D:\\New_Folder") # создает на диске 'D' директорию 'New_Folder'

# создать две папки (папку в папке) невозможно
# # os.mkdir(r"D:\folder\qwerty") # приведет к исключению FileNotFoundError)

# удаление файла. Создадим на диске D файл 'Test_del.txt', запустим программу и удалим этот файл
# os.remove("D:\\Test_del.txt")  

# удаление пустой директории (удалим только что созданную директорию 'New_Folder')
os.rmdir("D:\\New_Folder")

# удалить несколько пустых директорий. Создадим на диске D директорию 'folder', в ней директорию 'qwerty'
# и удалим их
# os.removedirs(r"D:\folder\qwerty"))

# запустить файл. Поместим в директорию вместе с исполняемым файлом файл Alert1.wav и запустим программу
# os.startfile("Alert1.wav")

# запустить файл. Поместим в директорию вместе с исполняемым файлом файл Dices.exe и запустим программу
# os.startfile("Dices.exe")

# показать имя файла (из директории с исполняемым файлом)
# print(os.path.basename("Dices.exe"))

# показать имя директории в котором лежит файл
# print(os.path.dirname("test\\Dices.exe"))

# размер файла
# print(os.path.getsize("Dices.exe"))

# создание и переименование директории
# os.mkdir("D:\\folder")
# os.rename("D:\\folder", "D:\\folder2")

# переименование сразу нескольких директорий
# # os.renames(r"D:\folder\qwerty", r"D:\folder2\qwerty2")

# показать содержимое директории
# print(os.listdir("D:\\Python"))

# итерирование директории и вывод на печать всех файлов
# for c_dir, dirs, files in os.walk("D:\\Python"):
#     for d in files:
#         print(d)

# информация о папке или файле
# print(os.stat("test.py"))

# выводит на печать объединенный путь
print(os.path.join("D:\\Python", "text.txt"))

# разделяет путь
print(os.path.split("D:\\Python\\text.txt"))

# # !!! Тестирование проводилось на os_windows. Не все команды модуля os работают точно так же на других os !!!

# # Пример для os_mac:
# # метода открыть файл
# # os.system("open Day_20.py")
