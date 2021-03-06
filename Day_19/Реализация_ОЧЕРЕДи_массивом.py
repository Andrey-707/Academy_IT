# Реализация ОЧЕРЕДи массивом.

# ОЧЕРЕДЬ - это структура денных, в которой получить доступ и удалить можно только тот элемент, который был
# добавлен первым (принцип FIFO, - First In First Out)

from rich import print
from time import sleep


# Пример_1. Метод присваивания значения A_Queue[i] = "-"

# ОЧЕРЕДЬ в виде массива. Изначально заполнена символом прочерка "-", далее, используя присваивиние символ "-"
# заменяем цифрами в формате строки.

n = 15 # колечесто элементов в ОЧЕРЕДи
A_Queue = ["-"]*n # ОЧЕРЕДЬ
h = 0 # голова/head ОЧЕРЕДи (элемент который был добавлен первым)
t = 0 # хвост/tail ОЧЕРЕДи (элемент который был добавлен последним)
print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# заполним ОЧЕРЕДЬ цифрами
for i in range(1, 10+1):
    A_Queue[t] = str(i) # добавим цифру в виде строки
    t = (t + 1) % n
    print(A_Queue)
    sleep(0.5)
# print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# заполним ОЧЕРЕДЬ цифрами ЕЩЁ РАЗ. Цифр больше чем размер ОЧЕРЕДи, но при условии, если t == 15 сработает break
for i in range(11, 20+1):
    A_Queue[t] = str(i) # добавим цифру в виде строки
    if t != n-1:
        t += 1 
        print(A_Queue)
        sleep(0.5)
    else:
        print(A_Queue)
        break
# print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# переменная stop_iter указывает когде закончить процедуру удаления символов из ОЧЕРЕДи
stop_iter = n # то есть при достижении значения ноль

# в голове ОЧЕРЕДи сейчас единица. Очистим ОЧЕРЕДЬ по принципу FIFO, - First In First Out)
while h != stop_iter:
    A_Queue[h] = "-"
    h += 1
    print(A_Queue)
    sleep(0.5)
print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}")

#################################################################################################################

# Пример_2. Методы .append() и .pop()

# ОЧЕРЕДЬ в виде массива. Изначально пустая [], далее, используя метод списка .append() заполняем цифрами в формате
# целого числа. Очистка ОЧЕРЕДи при помощи метода списка .pop(0) с индексом 0 (принцип FIFO, - First In First Out).

n = 15 # колечесто элементов в ОЧЕРЕДи
A_Queue = [] # ОЧЕРЕДЬ
h = 0 # голова/head ОЧЕРЕДи (элемент который был добавлен первым)
t = 0 # хвост/tail ОЧЕРЕДи (элемент который был добавлен последним)
print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# заполним ОЧЕРЕДЬ цифрами
for i in range(1, 10+1):
    A_Queue.append(i) # добавим число в ОЧЕРЕДЬ
    t = (t + 1) % n
    print(A_Queue)
    sleep(0.5)
# print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# заполним ОЧЕРЕДЬ цифрами ЕЩЁ РАЗ. Цифр больше чем размер ОЧЕРЕДи, но при условии, если t == 15 сработает break
for i in range(11, 20+1):
    A_Queue.append(i) # добавим число в ОЧЕРЕДЬ
    if t != n-1:
        t += 1 
        print(A_Queue)
        sleep(0.5)
    else:
        print(A_Queue)
        break
# print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}\n")

# переменная stop_iter указывает когде закончить процедуру удаления символов из ОЧЕРЕДи
stop_iter = t - n # то есть при достижении значения ноль

# в голове ОЧЕРЕДи сейчас единица. Очистим ОЧЕРЕДЬ по принципу FIFO, - First In First Out)
while t != stop_iter:
    A_Queue.pop(h)
    t -= 1
    print(A_Queue)
    sleep(0.5)
print(f"\n[bold yellow]A QUEUE[/]\n{A_Queue}")
