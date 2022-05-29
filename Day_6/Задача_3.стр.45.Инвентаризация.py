# Задача№3.стр.45.
# Склад: создать список словарей для инвентаризации чего-либо.

# Посчитаем некое "something"

from rich import print # для удобства визуализации


# пустой каталог
some_dict = {}

# входные дданные
key = 'something'
value = int(input(f"Сколько '{key}' у нас сейчас? "))

# из полученных данных формируем каталог
some_dict[key] = value

def inventory():
    '''Функция подсчитывает "something", добавляет их в переменную count и возвращает count'''
    count = 0
    while True:
        enter = input("Инвентаризируем 'something':\nвыход 'end'\nвызов справки 'help'\n")
        # если вводим значения по ключу из каталога, значение добавится в count
        if enter in some_dict:
            count += 1
            some_dict[enter] += 1
            print("[bold green]'something' has been added.[/]")
        # вызов просмотра каталога
        elif enter == "help":
            print("[bold green]View catalog.[/]")
            print(some_dict)
        # закончить добавление и выход при помощи ввода ключевого слова "end"
        elif enter == "end":
            print("Выход из программы.")
            break
        # ввод значения НЕ из каталога "some_dict" вызывает ошибку
        else:
            print("[bold red]Error! Это мы не инвентаризируем.[/]")

    return count


# run
print(f"[bold cyan]Добавлено '{key}':[/]", inventory())

# В данном примере приведен один словарь, если расширить функционал программы, можно создать несколько словарей
# и внести их в список.
print(f"[bold yellow]Итого:[/]\n{some_dict}")
