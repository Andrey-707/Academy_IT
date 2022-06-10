# Библиотека_collections.Класс_Counter

from collections import Counter


text = "Война и мир Л.Н. Толстой"

# Создадим экземпляр класса Counter(), передадим в него текст
c = Counter(text)

# Все элементы
# OUT: Counter({' ': 4, 'о': 3, 'й': 2, 'и': 2, '.': 2, 'В': 1, 'н': 1, 'а': 1,
#               'м': 1, 'р': 1, 'Л': 1, 'Н': 1, 'Т': 1, 'л': 1, 'с': 1, 'т': 1})
#print(c)

# все элементы с повторениями
#print(list(c.elements())) 
# OUT: ['В', 'о', 'о', 'о', 'й', 'й', 'н', 'а', ' ', ' ', ' ', ' ',
#       'и', 'и', 'м', 'р', 'Л', '.', '.', 'Н', 'Т', 'л', 'с', 'т']

# Часто встречающиеся элементы
#print(c.most_common())
# OUT: [(' ', 4), ('о', 3), ('й', 2), ('и', 2), ('.', 2), ('В', 1), ('н', 1), ('а', 1),
#       ('м', 1), ('р', 1), ('Л', 1), ('Н', 1), ('Т', 1), ('л', 1), ('с', 1), ('т', 1)]

# Все элементы без повторений
print(list(c.keys()))
# OUT: ['В', 'о', 'й', 'н', 'а', ' ', 'и', 'м', 'р', 'Л', '.', 'Н', 'Т', 'л', 'с', 'т']

########################################################################################################################

# Создадим экземпляр класса Counter(), передадим в него a=3, b=1
x = Counter(a=3, b=1)
# Создадим экземпляр класса Counter(), передадим в него a=1, b=2
y = Counter(a=1, b=2)

# Выводим на экран
print(x, y) # OUT: Counter({'a': 3, 'b': 1}) Counter({'b': 2, 'a': 1})

# Сумма по одинаковым ключам
print(x + y) # OUT: Counter({'a': 4, 'b': 3})

# Разность по одинаковым ключам
print(x - y) # OUT: Counter({'a': 2})

# Пересечение
print(x & y) # OUT: Counter({'a': 1, 'b': 1})

# Обьединение (ЭТО НЕ СУММА, это макс 'a' и макс 'b')
print(x | y) # OUT: Counter({'a': 3, 'b': 2})
