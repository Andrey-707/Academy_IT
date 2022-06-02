# Задача№3764.Частотный анализ.
# Дан текст. Выведите все слова, встречающиеся в тексте по одному на каждую строку. Слова должны быть отсортированы по
# убыванию их количества появления в тексте, а при одинаковой частоте появления - в логистическом порядке.

# Указание.
# Посте того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости
# слова и само слово. Например [(2, "hi"), (1, "what"), (3, "is")]. Тогда стандартная сортировка будет сортировать список
# кортежей, при этом кортежи сравниваются по первому элементу, а если они равны - то по второму. Это почти то, что 
# требуется в задаче.

# Входные данные:
# Вводится текст.

# Входные данные:
# Выведите ответ на задачу.

# Пример.

# Входные данные:
# Hi
# Hi
# What is your name
# My name is Bond
# James Bond
# My name is Damme
# Van Damme
# Claude Van Damme
# Jean Claude Van Damme

# Выходные данные:
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

# Решение.
from rich import print


# some string
some_string = """\
Hi!
Hi!
What is your name?
My name is Bond.
James Bond.
My name is Damme.
Van Damme.
Claude Van Damme.
Jean Claude Van Damme."""

print("[bold magenta]IN:[/]")
print(some_string)

# список символов, которые нужно удалять из текста
ban_list = ["!", "?", ".", "\n"]

# редактирование текста
for i in ban_list:
    # замена в тексте some_string символа на ПУСТОТУ, т.е. удаление его
    if i == "\n":
        some_string = some_string.replace(i, "")
    # замена в тексте some_string символа на ПРОБЕЛ    
    else:
        some_string = some_string.replace(i, " ")

# print(some_string) # на выходе получим строку из слов

# из строки создадим список слов
some_list = some_string.lower().split()
# print(some_list) # на выходе получим список из слов

# применим сортировку к списку some_list (В ТАКОМ МЕТОДЕ ДВЕ СОРТИРОВКИ, т.е. отсортированный по алфавиту
# список some_list сортируется снова по частоте появления слов и переворачивается в порядке убывания)
sorted_list = sorted(sorted(some_list), key=lambda x: some_list.count(x), reverse=True)
# print(sorted_list) # на выходе получим ДВАЖДЫ отсортированный список из слов

# отбросим повторяющиеся слова, результат сохраним в словарь result (повтор слова : слово)
result = {}
for i in sorted_list:
    if i not in result:
        count = 1
    else:
        count += 1
    result[i] = count

print("[bold magenta]\nOUT:[/]")
for k, v in result.items():
    print(f"{v} : {k}")

        
'''OUT:
4 : damme
3 : is   
3 : name 
3 : van  
2 : bond 
2 : claud
2 : hi   
2 : my   
1 : james
1 : jean 
1 : what 
1 : your 
'''


####################################################################################################
# Решение_2
def count_words(st):
    l1, l2, l3 = [], [], []
    d = {}
    for i in st.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in d:
        a = (d[j], j)
        l1.append(a)
    l1 = sorted(l1, reverse=True)
    q = l1[0][0]
    while len(l1) > len(l3):
        for b in l1:
            if b[0] == q:
                l2.append(b)
        if len(l2) > 1:
            l2 = sorted(l2)
            for m in l2:
                l3.append(m)
            l2 = []
        else:
            for m in l2:
                l3.append(m)
            l2 = []
        q -= 1
    return l3

# some string
some_string = """\
Hi!
Hi!
What is your name?
My name is Bond.
James Bond.
My name is Damme.
Van Damme.
Claude Van Damme.
Jean Claude Van Damme."""

# список символов, которые нужно удалять из текста
ban_list = ["!", "?", ".", "\n"]

# редактирование текста
for i in ban_list:
    # замена в тексте some_string символа на ПУСТОТУ, т.е. удаление его
    if i == "\n":
        some_string = some_string.replace(i, "")
    # замена в тексте some_string символа на ПРОБЕЛ
    else:
        some_string = some_string.replace(i, " ")

print("[bold magenta]IN:[/]")
print(some_string) # на выходе получим строку из слов

# повтор слова : слово
print("[bold magenta]\nOUT:[/]")
for res in count_words(some_string):
    print(f"{res[0]} : {res[1]}")

'''OUT:     
4 : Damme
3 : Van  
3 : is   
3 : name 
2 : Bond 
2 : Claud
2 : Hi   
2 : My   
1 : James
1 : Jean 
1 : What 
1 : your 
'''
