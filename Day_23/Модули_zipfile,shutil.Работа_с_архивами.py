# Модуль_zipfile, shutil. Работа с архивами.

import zipfile


# # У нас есть директория 'New_Folder', в которой лежит три тектовых файла 'File_1.txt', 'File_2.txt' и
# # 'File_3.txt'.Добавим диркторию в архив, архив назовем 'New_Archiver.zip'. Адрес архива запишем в 'path'.

# # путь к архиву
# path = r"D:\Python\Test\Python_Lessons\Академия_АйТи\Day_23\New_Archiver.zip"

# # ситываем данные из архива
# z = zipfile.ZipFile(path, "r")
# """OUT:
# New_Folder/ (2022, 6, 10, 17, 30, 16)
# New_Folder/File_1.txt (2022, 6, 10, 17, 29, 38)
# New_Folder/File_2.txt (2022, 6, 10, 17, 29, 38)
# New_Folder/File_3.txt (2022, 6, 10, 17, 30, 8)
# """
# for i in z.infolist():
#     print(i.filename, i.date_time)

# # У нас есть архив с именем 'New_Archiver2.zip'. Адрес архива запишем в 'path'. У нас есть
# # файл 'New_Py.py', этот файл находится в той же директории, что и исполняемый файл (тогда в архиве
# # будет записан просто файл). Если файл лежит по пути 'file_path', то внутрь архива помещается весь
# # путь до файла , внутри всех директорий будет файл 'New_Py.py'. Запустим программу.

# # путь к архиву
# path = r"D:\Python\Test\Python_Lessons\Академия_АйТи\Day_23\New_Archiver2.zip"
# # имя файла, который записываем в архив (записываемый файл в той же директории, что и исполняемый файл)
# file_name = "New_Py_1.py"
# # открываем архив на запись
# z = zipfile.ZipFile(path, "w")
# # записываем файл
# z.write(file_name)
# # закрываем, чтобы сохранить изменения
# z.close()
# # открываем архив на чтение, ситываем данные из архива (имя файлов и дату создания)
# z = zipfile.ZipFile(path, "r")
# for i in z.infolist():
#     print(i.filename) # OUT: New_Py.py

# # имя файла, который записываем в архив (записываемый файл находится в другой директории, что исполняемый файл)
# file_path = "D:\\Python\\Test\\Python_Lessons\\Академия_АйТи\\Day_23\\New_Py_2.py"
# # открываем архив на запись
# z = zipfile.ZipFile(path, "w")
# # записываем файл
# z.write(file_path)
# # закрываем, чтобы сохранить изменения
# z.close()
# # открываем архив на чтение, ситываем данные из архива
# z = zipfile.ZipFile(path, "r")
# for i in z.infolist():
#     print(i.filename) # OUT: Python/Test/Python_Lessons/Академия_АйТи/Day_23/New_Py_2.py

# # У нас есть архив с менем 'New_Archiver3.zip', он находится в той же директории, то и исполняемый файл.
# # проверим является ли он архивом, кроме того проверим является ли архивом исполняемый файл.
# f1 = "New_Archiver3.zip"
# print("{0}: {1}".format(f1, zipfile.is_zipfile(f1))) # OUT: New_Archiver3.zip: False
# f2 = "test.py"
# print("{0}: {1}".format(f2, zipfile.is_zipfile(f2))) # OUT: test.py: False

# # Создадим архив при помощи модуля 'zipfile'. У нас есть три текстовых файла, они лежат в той же директории,
# # что и исполняемый файл.
# with zipfile.ZipFile('New_Archiver4.zip', 'w') as zf:
#     zf.write('File_1.txt')
#     zf.write('File_2.txt')
#     zf.write('File_3.txt')

# # Если zip архив создан при помощи модуля 'zipfile', в случае проверки он вернет True
# print(zipfile.is_zipfile('New_Archiver4.zip')) # OUT: True

# Создание архива при помощи модуля 'shutil'

import shutil


# архивирование
zip_name = r"D:\Python\Test\Python_Lessons\Академия_АйТи\Day_23\New_archive"
# внутрь функции .make_archive() передаем 'имя архива', 'тип архива', 'папка для архивирования'
# shutil.make_archive(zip_name, "zip", zip_name)

# архив создан не при помощи модуля 'zipfile', программа вернет False
# print(zipfile.is_zipfile(zip_name)) # OUT: False

# копирование файла (указываем имя файла, директорию куда копируем файл)
# shutil.copy("test.py", r"D:\Python\test")

# копирование содержимого директории (указываем копируемую директорию и директорию куда копируем)
# shutil.copytree(r"D:\Python\Test\folder", "New_Dir")

# перенос файлов (директории должны быть заранее созданы и в директории folder Должедн быть файл Text.txt)
# shutil.move("folder\\Text.txt", "New_Dir")

# # удаление папки с содержимым
# shutil.rmtree("New_Dir")
