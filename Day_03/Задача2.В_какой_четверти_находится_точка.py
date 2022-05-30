# Задача2.стр.32. В какой четверти находится точка.

# Задача: В какой четверти находится точка?
# Пользователь вводит координаты точки x, y

# Если x > 0 и y > 0
#   print("Точка в I четверти")

# Иначе если x < 0 и y > 0
#   print("Точка во II четверти")

# Иначе если x < 0 и y < 0
#   print("Точка в III четверти")

# Иначе если x > 0 и y < 0
#   print("Точка в IV четверти")

# Иначе если x == 0
#   print("Точка на оси X")

# Иначе если y == 0
#   print("Точка на оси Y")

def f_x_y(x, y):
    '''Функция исключает нулевые координаты для точки'''
    assert x != 0 and y != 0, "Точка лежит на оси 'x'." if x == 0 else "Точка лежит на оси 'y'."
    return x, y


while True:
    # программа зациклена, для выхода ввести n
    try:
        escape = input("Продолжить программу y/n: ")
        if escape == "y":
            x = int(input("Координаты точки 'x': "))
            y = int(input("Координаты точки 'y': "))
            f_x_y(x, y)
            if y > 0:
                if x > 0:
                    print("Точка в I четверти.")
                else:
                    print("Точка во II четверти.")
            else:
                if x < 0:
                    print("Точка в III четверти.")
                else:
                    print("Точка в IV четверти.")
        elif escape == "n":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Введите y/n")
    except ValueError:
        print("ValueError! Введите число.")
    except AssertionError as a_ex:
        print("AssertionError!", a_ex)
