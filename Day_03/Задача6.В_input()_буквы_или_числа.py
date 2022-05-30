# Задача6.стр.41. В_input()_буквы_или_числа.

# Напишите программу Python, которая проверяет, является ли введенное значение строкой с символом
# алфавита или числом. Если строка содержит число, определите какой тип данных имеет число и отобразите
# пользователю.

# !!! данные, полученные через input() по типу являются строкой <class 'str'> будь то число или символ !!!

while True:
    try:
        # программа зациклена, для выхода ввести n
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            enter = input("Ввод: ")
            if enter.isdigit() == True:
                print(f"Строка '{enter}' состоит из цифр.")
                print(type(enter))
            elif enter.isalpha() == True:
                print(f"Строка '{enter}' состоит из букв.")
                print(type(enter))
            else:
                print(f"В строке '{enter}' смешанный тип данных.")
                print(type(enter)) 
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Вы ввели не число.")
