# Стр.30.Задача_ №3. Удаление заглавных символов из строки.

# Том хотел написать программу, которая будет удалять из строки все заглавные буквы. Для написания
# такой программы он воспользовался методом .replace(), который принимает два аргумента
# 1 - это символ, который нужно найти в строке, 
# 2 - это символ на который нужно заменить найденный символ
# Но его программа работает не корректно. Исправьте программу или напишите свой алгоритм решения.

# letters = "AFFasfGfFGLagsfuyaFYGSYGFSLsfasfFSFSFsasfFfsf"
# OUT:          asf f   agsfuya         sfasf     sasff sf


# Первый способ. Строка.
letters = "AFFasfGfFGLagsfuyaFYGSYGFSLsfasfFSFSFsasfFfsf"

# в одну строчку 
new_letters1 = "".join(i for i in letters if i.islower())

# Расшифровка решения
# new_letters1 = ""
# for i in letters:
#     if i.islower():
#        new_letters1 += "".join(i)

print(new_letters1) # OUT: asffagsfuyasfasfsasffsf


# Второй способ. Список.
letters = "AFFasfGfFGLagsfuyaFYGSYGFSLsfasfFSFSFsasfFfsf"

# в одну строчку 
new_letters2 = "".join([i for i in list(letters) if i.islower()])

# Расшифровка решения
# list_letters = list(letters)
# new_list = []
# for i in list_letters:
#     if i.islower():
#         new_list.append(i)
# new_letters2 = "".join(new_list)

print(new_letters2) # OUT: asffagsfuyasfasfsasffsf


# Третий способ. Поможем Тому. Удаление из строки всех заглавных букв.
letters = "AFFasfGfFGLagsfuyaFYGSYGFSLsfasfFSFSFsasfFfsf"

for letter in letters:
    letters = letters.replace(letter.upper(), "")

print(letters) # OUT: asffagsfuyasfasfsasffsf

