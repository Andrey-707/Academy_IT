# Библиотека tkinter. GUI. Калькулятор.

import tkinter as tk
import winsound

# from tkinter import messagebox, PhotoImage
from threading import Thread


##############
## COMMANDS ##
##############

def add_digit(digit:str):
    """Adds numbers to the Entry field"""
    value = calc.get()
    if value[0] == "0" and len(value) == 1: # если на экране ноль и полее ввода не пустое
        value = value[1:]
    calc['state'] = tk.NORMAL # разморозка окна
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED # заморозка окна

def add_operation(operation:str):
    """Adds numbers to the Entry field"""
    value = calc.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value: # если << число -> операция_вычисления -> число -> операция_вычисления >>
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

def calculate():
    """Calculate values"""
    value = calc.get()
    if value[-1] in "+-*/": # если событие: << число -> операция_вычисления -> None -> равно >>
        value += value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
        calc['state'] = tk.DISABLED
    except (NameError, SyntaxError): # актуально если НЕ применяется заморозка окна (исключает ввод символов)
        tk.messagebox.showinfo("Error", "Invalid number")
        calc.insert(0, 0)
        calc['state'] = tk.DISABLED
    except ZeroDivisionError: # исключает деление на ноль
        tk.messagebox.showinfo("Error", "Division by zero")
        calc.insert(0, 0)
        calc['state'] = tk.DISABLED

def unary_minus():
    """Reverses the sign of a number"""
    value = calc.get()
    calc['state'] = tk.NORMAL
    if value[0] != "-":
        calc.delete(0, tk.END)
        calc.insert(0, "-" + value)
        calc['state'] = tk.DISABLED
    else:   
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])
        calc['state'] = tk.DISABLED

# возвращает число с точкой (НЕ ЗАВЕРШЕНО)
def sqrt():
    """Square root of a number"""
    value = calc.get()
    value = str(int(value)**0.5)
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED
    # if str(value)[1] == "." and len(str(value)[2:]) == 1:
    #     calc['state'] = tk.NORMAL
    #     calc.delete(0, tk.END)
    #     calc.insert(0, str(int(value)))
    #     calc['state'] = tk.DISABLED

def backspace():
    """Remove last character"""
    value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value[:-1])
    calc['state'] = tk.DISABLED

def clear():
    """Clear values"""
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    calc['state'] = tk.DISABLED

def press_key(event):
    """Adds value from keyboard"""
    print(repr(event.char)) # раскомментировать если требуется показать ввод с клавиатуры в терминале
    if event.char.isdigit(): # digit 
        add_digit(event.char)
    elif event.char in "+-*/": # math operation
        add_operation(event.char)
    elif event.char == "=" or event.char == "\r": # "Enter" / "="
        calculate()
    elif event.char in "cCсС": # clear
        clear()
    elif event.char == "\x08": # backspace
        backspace()

def mouse_click(event):
    """Plays sound on mouse click"""
    def music():winsound.PlaySound(
        r"sound\mouse_click.wav", False)
    Thread(target=music, daemon=True).start()

#############
## BUTTONS ##
#############

def create_button(digit:str):
    """Creates digit buttons on the Main field"""
    return tk.Button(text=digit, bd=2, font=('Arial', 10), command=lambda: add_digit(digit)) # bd - толщина рамки

def create_operation_button(operation:str):
    """Creates math operation buttons on the Main field"""
    return tk.Button(text=operation, bd=2, font=('Arial', 10), command=lambda: add_operation(operation))

def create_calc_button(function:str):
    """Adds calculate function to the button '=' """
    return tk.Button(text=function, bd=2, font=('Arial', 15), command=calculate)

def create_sqrt_button(function:str):
    """Adds sqrt function to the button "√" """
    return tk.Button(text=function, bd=2, font=('Arial', 10), command=sqrt)

def creat_unary_minus_button(function:str):
    """Creates unary_minus buttons on the Main field"""
    return tk.Button(text=function, bd=2, font=('Arial', 10), command=unary_minus)

def creat_backspace_button(function:str):
    """Creates backspace buttons on the Main field"""
    return tk.Button(text=function, bd=2, font=('Arial', 10), command=backspace)

def create_clear_button(function:str):
    """Adds clear function to the button 'c' """
    return tk.Button(text=function, bd=2, font=('Arial', 10), command=clear)

###################
## MAIN FUNCTION ##
###################

def main():
    """Main function"""
    global window, calc

    window = tk.Tk()
    window.geometry('267x310') # разрешение окна
    window.title('My_Calculator') # шапка окна
    window.iconphoto(True, tk.PhotoImage(
        file=r"icon\Calculator.png")) # добавление собственной картинки в шапку
    window.resizable(height=False, width=False) # фиксирование размера окна (запрещает растягивание окна)
    window['bg'] = '#000000' # 000000 - черный цвет в HEX 

    window.bind('<Key>', press_key) # обработчик нажатия на клавиатуру

    window.bind('<1>', mouse_click) # обработчик нажатия на ЛКМ

    calc = tk.Entry(window, bd=2, justify=tk.RIGHT, font=('Consolas', 16), width=16) # justify - с левого или правого края
    calc.insert(0, '0') # при запуске в поле ввода число ноль
    calc['state'] = tk.DISABLED # заморозка окна
    calc.grid(column=0, row=0, stick='WE', columnspan=5, padx=(11,0), pady=(20,2)) # stick - прилипание к полюсам

    # кнопоки 1 строки
    # спец операции: "mc", "mr", "ms", "m+", "m-"
    create_button("MC").grid(column=0, row=1, stick='WENS', padx=(11,0), pady=2) # padx/pady - отступы
    create_button("MR").grid(column=1, row=1, stick='WENS', padx=2, pady=2)
    create_button("MS").grid(column=2, row=1, stick='WENS', padx=2, pady=2)
    create_button("M+").grid(column=3, row=1, stick='WENS', padx=2, pady=2)
    create_button("M-").grid(column=4, row=1, stick='WENS', padx=2, pady=2)

    # кнопоки 2 строки
    # спец операции: "←", "±", "√"
    creat_backspace_button("←").grid(column=0, row=2, stick='WENS', padx=(11,0), pady=2) # padx/pady - отступы
    creat_unary_minus_button("±").grid(column=3, row=2, stick='WENS', padx=2, pady=2)
    create_sqrt_button("√").grid(column=4, row=2, stick='WENS', padx=2, pady=2)
    # операция очистки поля ввода: "ce", "c"
    create_button("CE").grid(column=1, row=2, stick='WENS', padx=2, pady=2)
    create_clear_button("C").grid(column=2, row=2, stick='WENS', padx=2, pady=2)

    # кнопоки 3 строки
    # цифры: "7", "8", "9"
    create_button("7").grid(column=0, row=3, stick='WENS', padx=(11,0), pady=2) # padx/pady - отступы
    create_button("8").grid(column=1, row=3, stick='WENS', padx=2, pady=2)
    create_button("9").grid(column=2, row=3, stick='WENS', padx=2, pady=2)
    # математический символ: "/", "%"
    create_operation_button("/").grid(column=3, row=3, stick='WENS', padx=2, pady=2)
    create_operation_button("%").grid(column=4, row=3, stick='WENS', padx=2, pady=2)

    # кнопоки 4 строки
    # цифры: "4", "5", "6"
    create_button("4").grid(column=0, row=4, stick='WENS', padx=(11,0), pady=2)
    create_button("5").grid(column=1, row=4, stick='WENS', padx=2, pady=2)
    create_button("6").grid(column=2, row=4, stick='WENS', padx=2, pady=2)
    # математический символ: "*", "1/x"
    create_operation_button("*").grid(column=3, row=4, stick='WENS', padx=2, pady=2)
    create_operation_button("1/x").grid(column=4, row=4, stick='WENS', padx=2, pady=2)

    # кнопоки 5 строки
    # цифры: "1", "2", "3"
    create_button("1").grid(column=0, row=5, stick='WENS', padx=(11,0), pady=2)
    create_button("2").grid(column=1, row=5, stick='WENS', padx=2, pady=2)
    create_button("3").grid(column=2, row=5, stick='WENS', padx=2, pady=2)
    # математический символ: "-"
    create_operation_button("-").grid(column=3, row=5, stick='WENS', padx=2, pady=2)

    # кнопоки 6 строки
    # цифры: "0"
    create_button("0").grid(column=0, columnspan=2, row=6, stick='WENS', padx=(11,0), pady=2)
    # спец операции: ","
    create_button(",").grid(column=2, row=6, stick='WENS', padx=2, pady=2)
    # математический символ: "+"
    create_operation_button("+").grid(column=3, row=6, stick='WENS', padx=2, pady=2)
    # операция вычисления: "="
    create_calc_button("=").grid(column=4, row=5, rowspan=2,  stick='WENS', padx=2, pady=2)

    # задание минимальных размеров колонн
    window.grid_columnconfigure(0, minsize=30)
    window.grid_columnconfigure(1, minsize=30)
    window.grid_columnconfigure(2, minsize=30)
    window.grid_columnconfigure(3, minsize=30)
    window.grid_columnconfigure(4, minsize=30)

    # задание минимальных размеров строк
    window.grid_rowconfigure(1, minsize=40)
    window.grid_rowconfigure(2, minsize=40)
    window.grid_rowconfigure(3, minsize=40)
    window.grid_rowconfigure(4, minsize=40)
    window.grid_rowconfigure(5, minsize=40)
    window.grid_rowconfigure(6, minsize=40)

    # цикл
    window.mainloop()


# run
if __name__ == '__main__':
    main()
