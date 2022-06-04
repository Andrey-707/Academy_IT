# Реализация СТЕКа.
# Проверка на ровное количество открывающихся и закрывающихся скобок "()", "[]", "{}" в строке
# Если ровное, то печатаем yes, если неровное - no

from rich import print
from time import sleep


# Примеры под верное условие
s1 = "([{}])"
s2 = "([][]{})"

# Примеры под неверное условие
s3 = "([)]"
s4 = "([][]{}))"

# Пример под верное условие. С цифрами
s5 = "(1, 2, 3, [4, 5], {'a': 6})"

# Пример под неверное условие. С цифрами
s6 = "[2+(8+{8+7}+[7+9])]"

def parenthesis_check(s:str):
    '''Функция проверяет строку на правильность открывающих и закрывающих
    скобок "()", "[]", "{}" '''
    st = []  # стек
    correct = True
    # итерация по элементам строки (по символам)
    for i in s:
        sleep(1) 
        print("[bold green]STACK: [/]", st)

        # если скобка открывающая, то добавляем её в СТЕК
        if i in "({[":
            sleep(1)             
            print("[bold yellow]APPEND[/]", i, "[bold yellow]to the STACK[/]")
            st.append(i)

        # если элемент i не является скобкой, то пропускаем итерацию 
        elif i != "(" and i != "[" and i != "{" and i != ")" and i != "]" and i != "}":
            sleep(1)            
            print(i, "[bold magenta]continue[/]")
            continue
        # проерка СТЕКА на нулевую длину (нельзя ставить это условие в начало(в if) иначе программа сразу выходит в break)
        elif len(st) == 0:
            sleep(1)            
            print("[bold red]len(st) == 0\nbreak[/]")
            correct = False
            break

        # иначе если скобка не открывающая
        else: # i not in "({[":
            # отделить методом .pop() последнюю открывающую скобку из СТЕКА и записать её в переменную 'b'
            sleep(1) 
            print("[bold cyan]POP[/]", i, "[bold cyan]from the STACK[/]")            
            b = st.pop()
           
            # если в переменную 'b' записана открывающая скобка определенного вида и элемент i не является
            # закрывающей скобкой этого вида (т.е. следующая скобка в строке не закрывающая)
            if b == "(" and i != ")" or b == "{" and i != "}" or b == "[" and i != "]":
                sleep(1)            
                print(i, "[bold red]break[/]")
                correct = False
                break
    
    return "YES" if correct and len(st) == 0 else "NO"

#print(parenthesis_check(s1)) # yes
#print(parenthesis_check(s2)) # yes
#print(parenthesis_check(s3)) # no
#print(parenthesis_check(s4)) # no
#print(parenthesis_check(s5)) # yes
print(parenthesis_check(s6)) # yes
