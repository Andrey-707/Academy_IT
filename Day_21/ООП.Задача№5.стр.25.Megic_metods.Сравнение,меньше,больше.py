# Задача№5.стр.25.Megic_metods. Сравнение, меньше, больше.
# Строки в Python сравниваются на основании значений символов. Т.е. если мы захотим выяснить что больше:
# "Apple" или "Яблоко", то - "Яблоко" окажется бОльшим.
# А все потому, что английская буква "A" имеет значение 65 (из таблицы ASCII), а русская буква "Я" - 1071
# (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Яну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого она создает класс RealString и реализовывает озвученный ранее инструментарий. Сравнивать между
# собой можно как обьекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Яне понадобилось только три метода внутри класса (включая конструктор __init__()) для воплощения
# идеи.

# Решение:
class RealString:

    # КОНСТРУКТОР + три метода СРАВНЕНИЯ внутри класса
    def __init__(self, string):
        self.string = str(string)
        
    def __eq__(self, other):
        return len(self.string) == len(other.string)

    def __lt__(self, other):
        return len(self.string) < len(other.string)

    def __gt__(self, other):
        return len(self.string) > len(other.string)

# Создаем экземпляры класса RealString
some_str1 = RealString("Apple")
some_str2 = RealString("Яблоко")

# Применяем методы сравнения
print(some_str1 == some_str2) # OUT: False
print(some_str1 > some_str2) # OUT: False
print(some_str1 < some_str2) # OUT: True

# Возможно так же существующие строки передать при создании экземпляров класса

# строки
str1 = "Apple"
str2 = "Яблоко"

# создаемэкземпляры класса и передаемстроки
print(RealString(str1) == RealString(str2)) # OUT: False
print(RealString(str1) > RealString(str2)) # OUT: False
print(RealString(str1) < RealString(str2)) # OUT: True

# а ТАК сравнивать НЕЛЬЗЯ !!!
# print(RealString(str1) <= RealString(str2))
# OUT: TypeError: '<=' not supported between instances of 'RealString' and 'RealString'
