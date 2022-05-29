# Шахматная фигура "Слон".

# Требуется определить, бьёт ли "Слон", стоящий на клетке с указанными координатами (номер строки и столбца),
# фигуру, стоящую на другой указанной клетке.
# Входные данные
# Вводятся четыре числа: координаты "Слона" и координаты другой фигуры. Координаты - целые числа в интервале
# от 1 до 8.
# Выходные данные
# Требуется вывести слово "YES", если "Слон" может побить фигуру за 1 ход, в противном случае вывести "NO"

# Двигая "Слона" по шахматной клетки можно заметить, что слон всегда ходит по диагоналям квадрата, т.е. если
# по координате X он передвинется на 5 клеток то и по координате Y он передвинется на 5 клеток. Отсюда можем
# сделать вывод, что модуль разности координатов X1 и X2 и Y1 и Y2 всегда будет равен.

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
            # Например, Слон стоит на клетке 5:4
            x1 = int(input("Введите координаты 'Слона' по горизонтали: ")) # 5
            y1 = int(input("Введите координаты 'Слона' по вертикали: ")) # 4
            chess_board(x1, y1)
            # Например, "Шахматная фигура" стоит на клетке 7:6
            x2 = int(input("Введите координаты 'Шахматной фигуры' по горизонтали: ")) # 7
            y2 = int(input("Введите координаты 'Шахматной фигуры' по вертикали: ")) # 6
            chess_board(x2, y2)
            if  x1 != x2 or y1 != y2:
                # проверка (сравнение) на диагональное перемещение
                # модули изменения (дэльта) координат по оси x и по оси y равны
                if abs(x1 - x2) == abs(y1 - y2):
                    print("[bold green]YES[/]") 
                else:
                    print("[bold red]NO[/]")
            else:
                print("[bold red]Фигуры не могут стоять на одной клетке[/]")
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите число.")
    except AssertionError as a_ex:
        print("AssertionError!", a_ex)
