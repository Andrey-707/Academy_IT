# Напишите программу, которая на входе получает начальный и конечный символ. Отобразить строку начиная с
# начального символа и завершая конечным символом согласно таблице ASCII.

# Настройка кодировки шрифтов
# 1251 - Windows-кодировка. (Кириллица)
# 866 - DOS-кодировка
# 65001 - Кодировка UTF-8

from rich import print # для удобства визуализации


running = True
while running:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            symbol1 = int(input("Выводить ASCII с "))
            symbol2 = int(input("Выводить ASCII до "))
            for i in range(symbol1, symbol2+1):
                print("%4d-%s" % (i, chr(i)), end="")
                # после каждого 10 ого символа переводить строку
                if i % 10 == 0:
                    print()
            print()
        elif escape == "n":
            print("Выход из программы.")
            running = False
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите положительное число в качестве индекса.")


# Поиск конкретного символа в таблице ASCII
# Например, я ищу символ '№'. В месте итерации в условие прописываем конкретный символ 'if chr(i) == "№":'
# Далее в input() ввожу от 1 до 10000.
# В итоге: 8470-№

running = True
while running:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            symbol1 = int(input("Выводить ASCII с "))
            symbol2 = int(input("Выводить ASCII до "))
            for i in range(symbol1, symbol2+1):
                if chr(i) == "№":
                    print("%5d-%s"%(i,chr(i)), end="")
        elif escape == "n":
            print("Выход из программы.")
            running = False
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите положительное число в качестве индекса.")
