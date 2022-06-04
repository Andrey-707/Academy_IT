# Реализация СТЕКа массивом.

# СТЕК - это структура денных, в которой получить доступ и удалить можно только тот элемент, который был
# добавлен последним (принцип LIFO, - Last In First Out).

from rich import print
from time import sleep


# Пример_1. Метод присваивания значения A_stack[i] = "-"

# СТЕК в виде массива. Изначально заполнен символами прочерка "-", далее, используя присваивиние символ "-"
# заменяем цифрами в формате строки.

n = 15 # колечество элементов в СТЕКе
A_stack = ["-"]*n # СТЕК
h = 0 # голова СТЕКа (элемент который был добавлен первым)
print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# заполним СТЕК цифрами
for i in range(1, 10+1):
    A_stack[h] = str(i) # добавим цифру в виде строки
    if h != n-1:
        h += 1
        print(A_stack)
        sleep(0.5)
    else:
        print(A_stack)
        break

# print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# заполним СТЕК цифрами ЕЩЁ РАЗ. Цифр больше чем размер СТЕКа, но при условии, если h == n-1 == 14 сработает break
for i in range(11, 20+1):
    A_stack[h] = str(i) # добавим цифру в виде строки
    if h != n-1:
        h += 1
        print(A_stack)
        sleep(0.5)
    else:
        print(A_stack)
        break
# print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# переменная stop_iter указывает когде закончить процедуру удаления символов из СТЕКа
stop_iter = h - n # то есть при достижении значения ноль

# в голове СТЕКа сейчас число h = 15. Очистим СТЕК по принципу LIFO, - Last In First Out.
while h != stop_iter:
    A_stack[h] = "-"
    h -= 1
    print(A_stack)
    sleep(0.5)
print(f"\n[bold yellow]A STACK[/]\n{A_stack}")

#################################################################################################################

# Пример_2. Методы .append() и .pop()

# СТЕК в виде массива. Изначально пустой [], далее, используя метод списка .append() заполняем цифрами в формате
# целого числа. Очистка СТЕКа при помощи метода списка .pop() (принцип LIFO, - Last In First Out).

A_stack = [] # СТЕК
n = 15 # максимально дупустимое количество элементов в СТЕКе
h = 0 # голова СТЕКа (индекс элемена, который был добавлен первым)
print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# заполним СТЕК цифрами
for i in range(1, 10+1):
    A_stack.append(i) # добавим число в СТЕК
    if h != n-1:
        h += 1
        print(A_stack)
        sleep(0.5) 
    else:
        print(A_stack)
        break
# print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# заполним СТЕК цифрами ЕЩЁ РАЗ. Цифр больше чем размер СТЕКа, но при условии, когда h == n-1 == 14 сработает break
for i in range(11, 20+1):
    A_stack.append(i) # добавим цифру в виде строки
    if h != n-1:
        h += 1
        print(A_stack)
        sleep(0.5)
    else:
        print(A_stack)
        break
# print(f"\n[bold yellow]A STACK[/]\n{A_stack}\n")

# переменная stop_iter указывает когде закончить процедуру удаления символов из СТЕКа
stop_iter = h - n # то есть при достижении h значения ноль

# в голове СТЕКа сейчас число h = 15. Очистим СТЕК по принципу LIFO, - Last In First Out.
while h != stop_iter:
    A_stack.pop()
    h -= 1
    print(A_stack)
    sleep(0.5)
print(f"\n[bold yellow]A STACK[/]{A_stack}")
