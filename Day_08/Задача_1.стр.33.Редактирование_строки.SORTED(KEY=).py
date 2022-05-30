# Задача_1.стр.33.Редактирование_строки.SORTED(KEY=)
# Отсортировать слова в тексте по алфавиту, сохраняя регистр букв, но удаляя знаки препинания.
# Ввод:
# Добрый день, дорогие друзья! Сегодня ХОРОШАЯ погода!
# Вывод:
# день Добрый дорогие друзья погода Сегодня ХОРОШАЯ

some_string = "Добрый день, дорогие друзья! Сегодня ХОРОШАЯ погода!"
print("IN:", some_string)

some_list = sorted(some_string.split(), key=str.lower)

for i, j in enumerate(some_list):
    some_list[i] = j.strip(",!")

new_string = " ".join(some_list)
print("OUT:", new_string)

# ------------------------------------------Решение_в_одну_строчку------------------------------------
some_string = "Добрый день, дорогие друзья! Сегодня ХОРОШАЯ погода!"
print("IN:", some_string)

new_string = " ".join(i.strip(",!") for i in sorted(some_string.split(), key=str.lower))
print("OUT:", new_string)
