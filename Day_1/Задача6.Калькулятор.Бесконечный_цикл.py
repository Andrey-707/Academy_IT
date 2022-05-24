# Задача6. Калькулятор.Бесконечный цикл.

# Напишите программу Python, которая принимает два числа 'a' и 'b', далее находит сумму, 
# разность, произведение и деление 'a' на 'b'. В результате отобразите ответы для 
# каждой из арифметических операций.

# простой калькулятор работает бесконечно, пока в качестве арифметической
# операции пользователь не вводит ключевое слово 'END'.
operators = ["+", "-", "*", "/"]
while True:
    try:
        arithmetic = input("Введите арифметическую операцию? (+, -, *, /)\n" \
            "Для завершения программы введите 'END'\n")
        if arithmetic == "END":
            print("Выход из программы")
            break
        elif arithmetic in operators:
            a = int(input ("Введите первое число 'a': "))
            b = int(input ("Введите второе число 'b': "))
            if arithmetic == operators[0]:
                r = a + b
                print(f"Результат: {r}\n")
            elif arithmetic == operators[1]:
                r = a - b
                print(f"Результат: {r}\n")
            elif arithmetic == operators[2]:
                r = a * b
                print(f"Результат: {r}\n")
            elif arithmetic == operators[3]:
                r = a / b
                print(f"Результат: {r}\n")
        else:
            print("Error! Выбрана недопустимая операция!\n")
    except ValueError:
        print("ValueError! Вы ввели не число!\n")
