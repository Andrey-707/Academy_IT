# Шахматная фигура "Конь".

# Требуется определить, бьёт ли "Конь", стоящий на клетке с указанными координатами (номер строки и столбца),
# фигуру, стоящую на другой указанной клетке.
# Входные данные
# Вводятся четыре числа: координаты "Коня" и координаты другой фигуры. Координаты - целые числа в интервале
# от 1 до 8.
# Выходные данные
# Требуется вывести слово "YES", если "Конь" может побить фигуру за 1 ход, в противном случае вывести "NO"

# Проанализировав ход "Коня" буквой "Г" можно увидеть что если "Конь" ходит вниз или вверх буквой то его
# координата по X меняется на 1 а координата по Y на 2, если влево и вправо то наоборот X на 2 а Y на 1. Исходя
# из этого можно написать код, что если разность координат X1 и X2 уменьшилась или увеличилась на 1 и при этом
# разность координат Y1 и Y2 уменьшалась или увеличилась на 2 или если разность координат X1 и X2 уменьшилась
# или увеличилась на 2 и при этом разность координат Y1 и Y2 уменьшалась или увеличилась на 1 то выводим YES
# иначе NO.

from rich import print # для удобства визуализации


def chess_board(x, y):
    '''Функция ограничивает значения по горизонтали и вертикали от 1 включительно до 8 включительно'''
    assert 1 <= x <= 8 and 1 <= y <= 8, "Размеры шахматной доски 8 на 8 клеток."
    return x, y


while True:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            # Например, "Конь" стоит на клетке 5:4
            x1 = int(input("Введите координаты 'Коня' по горизонтали: ")) # 5
            y1 = int(input("Введите координаты 'Коня' по вертикали: ")) # 4
            chess_board(x1, y1)
            # Например, "Шахматная фигура" стоит на клетке 7:5
            x2 = int(input("Введите координаты 'Шахматной фигуры' по горизонтали: ")) # 7
            y2 = int(input("Введите координаты 'Шахматной фигуры' по вертикали: ")) # 5
            chess_board(x2, y2)
            if  x1 != x2 or y1 != y2:
                # изменение (дэльта) координат по оси x на 1 и изменение (дэльта) координат по y на 2 или наоборот
                if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
                    print("[bold green]YES[/]")
                else:
                    print("[bold red]NO[/]")
            else:
                print("[bold red]Фигуры не могут стоять на одной клетке![/]")
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите число.")
    except AssertionError as a_ex:
        print("AssertionError!", a_ex)
