# Задача.стр.38. Построчный вывод данных о пользователе.

# Напишите программу Python, которая отображала бы ваши данные, такие как имя, возраст, адрес,
# в трех разных строках. Например, чтобы она вывела:

# Name = Alex
# Age = 25
# Adress = Moscow, Tverskaya 1

Name = "Alex"
Age = 25
Adress = "Moscow, Tverskaya 1"

# 1_способ. С использованием переменных.
print("Name", Name, sep=" = ")
print("Age", Age, sep=" = ")
print("Adress", Adress, sep=" = ")

print() # пустая строка

# 2_способ. С использованием переменных. В одну строку (f-строка).
print(f"Name = {Name}\nAge = {Age}\nAddress = {Adress}")

print() # пустая строка

# 3_способ. Словарь.
some_dict = dict(Name=Name, Age=Age, Adress=Adress)

for key, value in some_dict.items():
    print(key, value, sep=" = ")
