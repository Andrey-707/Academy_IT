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
w.tracer(n=1, delay=0) # ЕСЛИ delay=0 - МГНОВЕННАЯ ОТРИСОВКА
w.bgcolor("forestgreen")

# button-turtle
btn = turtle.Turtle()
btn.width(1)
#btn.hideturtle()

# turtle
t = turtle.Turtle()
t.width(3)
#t.hideturtle()

# start ghost floor
n_floor = 3

# start ghost position
ghost = randint(1, 3)
print("ghost", ghost)
def prepare_figure(f, x, y):
    """place turtle on x and y"""
    f.shape("turtle")
    f.penup()
    f.goto(x, y)
    f.down()

def draw_button(x2, y2, fd1, fd2, tn):
    """drawing button 'start' """
    prepare_figure(btn, -50, 0)
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
    btn.hideturtle()

def keyword_up_button_press():
    """if button 'UP' pressed"""
    global button
    print("Button 'UP' pressed")
    btn.clear()
    button = False

def draw_landscape():
    """drawing landscape"""
    # земля
    prepare_figure(t, -250, -150)
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
    prepare_figure(t, -250, 150)
    t.fillcolor("#285078")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()

    btn.color("black")
    prepare_figure(btn, 0, 90)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    # верхняя граница
    t.rt(90)
    prepare_figure(t, -250, 50)
    t.fd(500)
    prepare_figure(btn, 0, -10)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    # нижняя граница
    prepare_figure(t, -250, -50)
    t.fd(500)
    prepare_figure(btn, 0, -115)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))
    # солнышко
    # круг
    prepare_figure(t, 200, 200)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(360):
        t.fd(0.5)
        t.lt(1)
    t.end_fill()
    # луч1
    t.lt(180)
    prepare_figure(t, 160, 235)
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
    prepare_figure(t, 165, 210)
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
    prepare_figure(t, 187, 193)
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
    prepare_figure(t, 215, 193)
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
    # верхний яру
    # 1 люк
    prepare_figure(t, -200, 140)
    t.lt(90)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    prepare_figure(t, -40, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    prepare_figure(t, 120, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # средний ярус
    # 1 люк
    prepare_figure(t, -200, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    prepare_figure(t, -40, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    prepare_figure(t, 120, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # нижний ярус
    # 1 люк
    prepare_figure(t, -200, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 2 люк
    prepare_figure(t, -40, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()
    # 3 люк
    prepare_figure(t, 120, -60)
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
    btn.color("black")
    prepare_figure(btn, 0, 90)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    prepare_figure(btn, 0, -10)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    prepare_figure(btn, 0, -115)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))

def game(what):
    """win of loose"""
    if what == True:
        w.clear()
        w.bgcolor("black")
        prepare_figure(t, -100, 0)
        t.color("green")
        t.write("Победа", font=("Courier", 30, "bold"))
    elif what == False:
        w.clear()
        w.bgcolor("black")
        prepare_figure(t, -200, 0)
        t.color("red")
        t.write("Вы проиграли", font=("Courier", 30, "bold"))

def get_pos(x, y):
    """get position"""
    print(x, y)
    global n_floor, ghost, what
    n_door = 0
    if -200 <=x<=-120 and 35*(n_floor-1)-170<= y<=35*(n_floor-1)-100:
        #btn.clear()
        print("1 door")
        n_door = 1
    elif -40<= x<= 40 and 35*(n_floor-1)-170<= y<=35*(n_floor-1)-100:
        #btn.clear()
        print("2 door")
        n_door = 2
    elif 120 <=x<= 200 and 35*(n_floor-1)-170<= y<= 35*(n_floor-1)-100:
        #btn.clear()
        print("3 door")
        n_door = 3
    
    if ghost == n_door:
        print("Попался!")
        t.color("#ff0000")
        ghost = randint(1, 3)
        print("ghost", ghost)
        n_floor -= 1
        # what = False
        # game(what)
    else:
        print("Вы перешли на другой уровень")
        t.color("#00ff00")
        ghost = randint(1, 3)
        print("ghost", ghost)
        n_floor -= 1
        # if n_floor == 0:
        #     what = True
        #     game(what)

    t.begin_fill()
    if n_door == 1:
        prepare_figure(t, -200, 35*(n_floor-1)-95)
    elif n_door == 2:
        prepare_figure(t, -40, 35*(n_floor-1)-95)
    elif n_door == 3:
        prepare_figure(t, 120, 35*(n_floor-1)-95)
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