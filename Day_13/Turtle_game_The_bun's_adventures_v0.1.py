# Barsukov Andrey
# Turtle game The bun's adventures
# Барсуков Андрей
# Turtle игра Приключения колобка

import turtle

from random import randint


def prepare(fig, x, y):
    """описание функции"""
    t.width(3)
    t.penup()
    t.goto(x, y)
    t.down()
    print("Prepeared")
    
def draw_button(x1, y1, x2, y2, fd1, fd2, tn):
    """отрисовка кнопки 'start' """
    btn.penup()
    btn.goto(x1, y1)
    btn.pendown()
    btn.fillcolor("green")
    btn.begin_fill()
    for i in range(2):
        btn.fd(fd1)
        btn.lt(tn)
        btn.fd(fd2)
        btn.lt(tn)
    btn.end_fill()
    btn.penup()
    btn.goto(x2, y2)
    btn.pencolor("white")
    btn.write("Start", font=("Arial", 12, "normal"))

# def mouse_l_button_click(x, y): # функция не используется
#     """если кнопка 'start' нажата, выполняй действия"""
#     if -50 < x < 30 and 0 < y < 30:
#         print("Button pressed")
#         btn.clear()

def keyword_up_button_press():
    """если кнопка 'UP' нажата, выполняй действия"""
    global button
    print("Button 'UP' pressed")
    btn.clear()
    button = False

def draw_landscape():
    """drawing landscape"""
    # земля
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()
    # небо
    t.penup()
    t.goto(-250, 150)
    t.lt(90)
    t.down()
    t.fillcolor("#285078")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()
    # верхняя граница
    t.penup()
    t.goto(-250, 50)
    t.rt(90)
    t.down()
    t.fd(500)
    # нижняя граница
    t.penup()
    t.goto(-250, -50)
    t.down()
    t.fd(500)
    
def draw_hatches():
    """drawing field"""
    # верхний ярус
    # 1 люк
    t.penup()
    t.goto(-200, 135)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 2 люк
    t.penup()
    t.goto(-40, 135)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 3 люк
    t.penup()
    t.goto(120, 135)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # средний ярус
    # 1 люк
    t.penup()
    t.goto(-200, 35)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 2 люк
    t.penup()
    t.goto(-40, 35)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 3 люк
    t.penup()
    t.goto(120, 35)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # нижний ярус
    # 1 люк
    t.penup()
    t.goto(-200, -65)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 2 люк
    t.penup()
    t.goto(-40, -65)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()
    # 3 люк
    t.penup()
    t.goto(120, -65)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()

def exit_game():
    """exit game"""
    w.bye()

def close():
    """описание функции"""
    close = turtle.Turtle()
    close.speed(0)
    #close.color("white") # поменять цвет строки, по умолчанию "black"
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 12, "bold"))
    w.listen()
    w.onkeypress(exit_game, "Escape")

def get_pos(x, y):
    """get position"""
    global n_door, ghost, n_floor, what
    
    if n_floor == 3:
        if -200 <= x <= -120 and -65 <= y <= -35:
            print("3d floor, 1st hatch")
            n_door = 1
        elif -40 <= x <= 40 and -65 <= y <= -35:
            print("3d floor, 2nt hatch")
            n_door = 2
        elif 120 <= x <= 200 and -65 <= y <= -35:
            print("3d floor, 3st hatch")
            n_door = 3
    elif n_floor == 2:
        if -200 <= x <= -120 and 35 <= y <= 35:
            print("3d floor, 1st hatch")
            n_door = 1
        elif -40 <= x <= 40 and 35 <= y <= 35:
            print("3d floor, 2nt hatch")
            n_door = 2
        elif 120 <= x <= 200 and 35 <= y <= 35:
            print("3d floor, 3st hatch")
            n_door = 3
    elif n_floor == 1:
        if -200 <= x <= -120 and 135 <= y <= 165:
            print("3d floor, 1st hatch")
            n_door = 1
        elif -40 <= x <= 40 and 135 <= y <= 165:
            print("3d floor, 2nt hatch")
            n_door = 2
        elif 120 <= x <= 200 and 135 <= y <= 165:
            print("3d floor, 3st hatch")
            n_door = 3

    if n_door == ghost:
        print("Попался!")
        what = False
        game(False)
    elif n_door != ghost:
        print("Вы выбрались с этажа", n_floor)
        n_floor -= 1
        ghost = randint(1, 3)
        print("ghost", ghost)
        if n_floor == 0:
            what = True
            game(True)
    else:
        pass        
# def change_floor(x, y): # функция не используется
#     """change floor"""
#     get_pos(x, y)
    
def game(what):
    """game"""
    if what == True:
        w.clear()
        w.bgcolor("black")
        t.color("green")
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write("Победа", font=("Courier", 30, "bold"))
    elif what == False:
        w.clear()
        w.bgcolor("black")
        t.color("red")
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        t.write("Вы проиграли", font=("Courier", 30, "bold"))

# window
w = turtle.Screen()
w.title("Game 'The bun's adventures'")
w.setup(500, 500)
w.tracer(n=1, delay=5) # (0) # ЕСЛИ 0 - МГНОВЕННАЯ ОТРИСОВКА 

# turtle
t = turtle.Turtle()
t.hideturtle()

# button 'start'
btn = turtle.Turtle()
btn.hideturtle()

# drawing button 'start'
draw_button(-50, 0, -30, 5, 80, 30, 90)

button = True
while button:
    w.update()
    turtle.listen()
    turtle.onkeypress(lambda: keyword_up_button_press(), 'Up') # обработка нажатой кнопки. <<функция, кнопка>>

# start floof number
n_floor = 3
n_door = 0

# start ghost position
ghost = randint(1, 3)
print("ghost", ghost)

turtle.listen()

prepare(t, -250, -150)
# drawing landscape
draw_landscape()

# drawing hatches
draw_hatches()

# check position
t.screen.onclick(get_pos)

w.listen()
w.onkeypress(close, "Escape") # выход из игры при нажатии клавиши "Esc"
turtle.done()