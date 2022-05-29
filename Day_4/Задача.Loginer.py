# Стр.29.Задача_ №1. Loginer

# Напишите программу, которая имитирует проверку пароля, придуманного пользователем.
# В переменной 'password' хранится правильный пароль.
# Пользователь вводит слово. Если оно совпадает с паролем, программа отвечает "Вы вошли в аккаунт",
# если не совпадает - пользователь вновь вводит слово.

password = "Andrey07"
running = True

while running:
    guess = input("Enter password: ")
    if guess == password:
        print( "Вы вошли в аккаунт")
        running = False
    else:
        print("Error! Retry.")

# Стр.29.Задача_ №2.
# добавьте для предыдущей задачи количество попыток ввода пароля. Если пользователь превысит это
# количество, то программа сообщит об этом и закончит работу.

password = "Andrey07"
running = True
repeat = 3

while repeat > 0:
    guess = input("Enter password: ")
    if guess == password:
        print("Вы вошли в аккаунт")
        break
    else:
        print("Error! Retry.")
    repeat -= 1
else:
   print("Access closed.") 
