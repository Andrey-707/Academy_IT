# Barsukov Andrey
# Turtle game The bun's adventures
# Барсуков Андрей
# Turtle игра Приключения колобка

import turtle

from random import randint


# window
w = turtle.Screen()
w.title("Game 'The bun's adventures'")
w.setup(500, 500)
w.tracer(0) # ЕСЛИ 0 - МГНОВЕННАЯ ОТРИСОВКА или (n=1, delay=25)
w.bgcolor("forestgreen")

# turtle
t = turtle.Turtle()
t.width(3)
t.shape("turtle")
#t.hideturtle()

# # button-turtle
# btn = turtle.Turtle()
# btn.width(1)
# #btn.hideturtle()

#start ghost position
ghost = randint(1, 3)
print("ghost", ghost)

def gt(x, y):
    """place turtle on x and y"""
    t.penup()
    t.goto(x, y)
    t.down()

def draw_button(x2, y2, fd1, fd2, tn):
    """drawing button 'start' """
    gt(-50, 0)
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
        t.fd(fd1)
        t.lt(tn)
        t.fd(fd2)
        t.lt(tn)
    t.end_fill()
    gt(x2, y2)
    t.pencolor("white")
    t.write("Start", font=("Arial", 12, "normal"))
    t.hideturtle()

def keyword_up_button_press():
    """if button 'UP' pressed"""
    global button
    print("Button 'UP' pressed")
    t.clear()
    button = False

def draw_landscape():
    """drawing landscape"""
    # земля
    t.pencolor("black")
    gt(-250, -150)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()
    # небо
    t.lt(90)
    gt(-250, 150)
    t.fillcolor("#285078")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()

    t.color("black")
    gt(0, 90)
    t.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    # верхняя граница
    t.rt(90)
    gt(-250, 50)
    t.fd(500)
    gt(0, -10)
    t.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    # нижняя граница
    gt(-250, -50)
    t.fd(500)
    gt(0, -115)
    t.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))
    # солнышко
    # круг
    gt(200, 200)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(360):
        t.fd(0.5)
        t.lt(1)
    t.end_fill()
    # луч1
    t.lt(180)
    gt(160, 235)
    t.width(2)
    t.color("black")
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()
    # луч2
    gt(165, 210)
    t.width(2)
    t.color("black")
    t.fillcolor("Yellow")
    t.begin_fill()
    t.lt(30)
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()
    gt(187, 193)
    t.width(2)
    t.color("black")
    t.fillcolor("Yellow")
    t.begin_fill()
    # луч3
    t.lt(30)
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()
    gt(215, 193)
    t.width(2)
    t.color("black")
    t.fillcolor("Yellow")
    t.begin_fill()
    # луч4
    t.lt(30)
    for i in range(2):
        t.fd(25)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()

def hatch():
    """описание функции"""
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)

def draw_hatches():
    """drawing field"""
    t.color("black")
    # верхний ярус
    # 1 люк
    gt(-200, 140)
    t.lt(90)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    gt(-40, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    gt(120, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # средний ярус
    # 1 люк
    gt(-200, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    gt(-40, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    gt(120, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # нижний ярус
    # 1 люк
    gt(-200, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    gt(-40, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    gt(120, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

def quit_game():
    """exit from the game"""
    w.bye()

def close():
    """if button 'esc' pressed check funktion exit_game"""
    close = turtle.Turtle()
    close.speed(0)
    #close.color("white") # поменять цвет строки, по умолчанию "black"
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 12, "bold"))
    w.listen()
    w.onkeypress(quit_game, "Escape")

def draw_level():
    """drawing levels"""
    t.color("black")
    gt(0, 90)
    t.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    gt(0, -10)
    t.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    gt(0, -115)
    t.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))

def game(what):
    """win of loose"""
    if what == True:
        w.clear()
        w.bgcolor("black")
        gt(-100, 0)
        t.color("green")
        t.write("Победа", font=("Courier", 30, "bold"))
    elif what == False:
        w.clear()
        w.bgcolor("black")
        gt(-200, 0)
        t.color("red")
        t.write("Вы проиграли", font=("Courier", 30, "bold"))

# start ghost floor
n_floor = 3
what = None

def get_pos(x, y):
    """get position"""
    global n_floor, ghost, what
    print(x, y, n_floor)
    n_door = 0
    if -200<=x<=-120 and 20*(n_floor)-100<=y<=20*(n_floor-1)-80: # -60-40 40 60 140 160
        #btn.clear()
        print("1 door")
        n_door = 1
    elif -40<=x<= 40 and 20*(n_floor-1)-100<=y<=20*(n_floor-1)-80:
        #btn.clear()
        print("2 door")
        n_door = 2
    elif 120<=x<=200 and 20*(n_floor-1)-100<=y<=20*(n_floor-1)-80:
        #btn.clear()
        print("3 door")
        n_door = 3

    if ghost == n_door:
        print("Попался!")
        t.color("#ff0000")
        ghost = randint(1, 3)
        print("ghost", ghost)
        n_floor += 1
        what = False
        game(what)
    elif ghost != n_door:
        print("Вы перешли на другой уровень")
        t.color("#00ff00")
        ghost = randint(1, 3)
        print("ghost", ghost)
        n_floor += 1
        if n_floor == 6:
            what = True
            game(what)

    t.begin_fill()
    if n_door == 1:
        gt(-200, 35*(n_floor-1)-165)
    elif n_door == 2:
        gt(-40, 35*(n_floor-1)-165)
    elif n_door == 3:
        gt(120, 35*(n_floor-1)-165)
    hatch()
    t.end_fill()

# drawing button 'start'
draw_button(-30, 5, 80, 30, 90)

button = True
while button:
    w.update()
    turtle.listen()
    turtle.onkeypress(keyword_up_button_press, 'Up') # обработка нажатой кнопки. <<функция, кнопка>>

turtle.onkeypress(draw_level, 'Down')

turtle.listen()

# drawing landscape
draw_landscape()

# drawing hatches
draw_hatches()

# check position
t.screen.onclick(get_pos)

w.update()
w.listen()
w.onkeypress(close, "Escape") # выход из игры при нажатии клавиши "Esc"
#turtle.done()
w.mainloop()