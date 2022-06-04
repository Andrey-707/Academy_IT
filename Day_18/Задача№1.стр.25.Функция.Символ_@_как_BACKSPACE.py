# Задача№1.стр.25.Удаление_символов_из_строки
# Александр решил каким-то образом отобразить в тексте BACKSPACE (т.е. удаление последнего символа).
# Он подумал, что символ <<@>> отлично для этого подходит.
# Напишите функцию cleaned_str(st), которая будет выполнять BACKSPACE в его строках:
# гр@оо@лк@оц@ва -> голова
# сварка@@@@лоб@ну@ -> слон

# print(clean_str(гр@оо@лк@оц@ва))
# print(clean_str(сварка@@@@@лоб@ну@))


from rich import print


# Решение_1. Срез строки, стрковый метода .count()

def cleaned_str(st:str):
    '''Функция удаляет из строки символы, если они находятся перед символом "@" так,
    словно "@" выполняет команду "backspace" '''
  
    # если "@" не первый символ в строке
    if st[0] != "@":
        for i in range(st.count("@")): # количество итераций равно количеству символов удаления '@' в строке
            st = st[:st.find("@")-1] + st[st.find("@")+1:]
    
    # если "@" первый символ в строке
    else:
        # срезаем строку с индекса 1 и до конца и дальше обрабетываем по прежней схеме
        st = st[1:]
        for i in range(st.count("@")): # количество итераций равно количеству символов удаления '@' в строке
            st = st[:st.find("@")-1] + st[st.find("@")+1:]
    
    # возвращаем строку
    return st


# RUN
some_string1 = "@гр@оо@лк@оц@ва"
print("[bold magenta]IN:[/]")
print(some_string1)

print("[bold magenta]OUT:[/]")
print(cleaned_str(some_string1)) # OUT: голова

some_string2 = "сварка@@@@@лоб@ну@"
print("[bold magenta]IN:[/]")
print(some_string2)

print("[bold magenta]OUT:[/]")
print(cleaned_str(some_string2)) # OUT: слон


# Решение_2. Список, метод списка .pop()

def cleaned_str(st):
    '''Функция добавляет в пустой список элементы из строки, если элемент является "@", то
    функция применяте метод .pop() к списку, тем самым удаляет последний элемент списка'''
    lst = []
    for i in st:
        # если элемент не является "@", то добавляем элемент к списку
        if i != "@":
            lst.append(i)

        # если элемент является "@" и список не пуст (lst == True), то удаляем элемент из списка (выполняем .pop())
        elif i == "@" and lst:
            lst.pop()

        # иначе пропускаем итерацию
        else:
            continue
        # print(f"[bold yellow]Список lst[/]\n{lst}")

    # возвращаем строку
    return "".join(lst)


# RUN
some_string1 = "@гр@оо@лк@оц@ва"
print("[bold magenta]IN:[/]")
print(some_string1)

print("[bold magenta]OUT:[/]")
print(cleaned_str(some_string1))

print("[bold magenta]IN:[/]")
some_string2 = "сварка@@@@@лоб@ну@"
print(some_string2)

print("[bold magenta]OUT:[/]")
print(cleaned_str(some_string2))
