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
w.tracer(n=1, delay=5) # ЕСЛИ delay=0 МГНОВЕННАЯ ОТРИСОВКА
w.bgcolor("forestgreen")

# turtle
t = turtle.Turtle()
t.width(3)
t.shape("turtle")
t.hideturtle()

# button-turtle
btn = turtle.Turtle()
btn.width(1)
btn.shape("circle")
btn.hideturtle()

#start ghost position
ghost = randint(1, 3)
print("ghost", ghost)

def gt(T, x, y):
    """put turtle on x and y"""
    T.penup()
    T.goto(x, y)
    T.down()

def draw_button(x, y, f_x, f_y, tn):
    """draw button 'start' """
    gt(btn, -50, 0)
    btn.fillcolor("green")
    btn.begin_fill()
    for i in range(2):
        btn.fd(f_x)
        btn.lt(tn)
        btn.fd(f_y)
        btn.lt(tn)
    btn.end_fill()
    gt(btn, x, y)
    btn.pencolor("white")
    btn.write("START", font=("Arial", 12, "normal"))
    btn.hideturtle()

def keyword_button_press():
    """if button '1' pressed removes all BTN (btn = turtle.Turtle()) captions """
    global pause
    print("Button '1' pressed")
    btn.clear()
    pause = False

def draw_landscape():
    """draw landscape"""
    # земля
    t.pencolor("black")
    gt(t, -250, -150)
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
    gt(t, -250, 150)
    t.fillcolor("#285078")
    t.begin_fill()
    for i in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()

    btn.color("black")
    gt(btn, 0, 90)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья

    # верхняя граница
    t.rt(90)
    gt(t, -250, 50)
    t.fd(500)
    gt(btn, 0, -10)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья

    # нижняя граница
    gt(t, -250, -50)
    t.fd(500)
    gt(btn, 0, -115)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья

    # солнышко
    # круг
    gt(t, 200, 200)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(180):
        t.fd(1)
        t.lt(2)
    t.end_fill()

    # луч1
    t.lt(180)
    gt(t, 160, 235)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()

    # луч2
    t.lt(30)
    gt(t, 165, 210)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()

    # луч3
    gt(t, 187, 193)
    t.fillcolor("Yellow")
    t.begin_fill()
    t.lt(30)
    for i in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()

    # луч4
    t.lt(30)
    gt(t, 215, 193)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(25)
        t.rt(90)
        t.fd(4)
        t.rt(90)
    t.end_fill()

def hatch():
    """draw a color rectangle"""
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)

def draw_hatches():
    """draw game field"""
    t.color("black")

    # верхний ярус
    # 1 люк
    gt(t, -200, 140)
    t.lt(90)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 2 люк
    gt(t, -40, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 3 люк
    gt(t, 120, 140)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # средний ярус
    # 1 люк
    gt(t, -200, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 2 люк
    gt(t, -40, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 3 люк
    gt(t, 120, 40)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # нижний ярус
    # 1 люк
    gt(t, -200, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 2 люк
    gt(t, -40, -60)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(20)
        t.lt(90)
    t.end_fill()

    # 3 люк
    gt(t, 120, -60)
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

def draw_stage_levels():
    """draw levels"""
    print("Button '2' pressed")
    btn.color("black")
    gt(btn, 0, 90)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    gt(btn, 0, -10)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    gt(btn, 0, -115)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))

def game(what):
    """win of loose"""
    if what == True:
        w.clear()
        w.bgcolor("black")
        gt(t, -100, 0)
        t.color("green")
        t.write("Победа", font=("Courier", 30, "bold"))
    elif what == False:
        w.clear()
        w.bgcolor("black")
        gt(t, -200, 0)
        t.color("red")
        t.write("Вы проиграли", font=("Courier", 30, "bold"))

# start options
n_floor = 3
what = None
delta_y = 0

def get_pos(x, y):
    """get position"""
    global n_floor, ghost, what, delta_y
    print(x, y, n_floor)
    n_door = 0
    # ---------- ИНТЕРВАЛ КООРДИНАТ ДЛЯ ПОЛУЧЕНИЯ n_door ПО Y ОТ И ДО (-60 -40; 40 60; 140 160) -------------
    # if -200 <= x <=-120 and -60 <= y <= -40:
    #     #btn.clear()
    #     print("1 door")
    #     n_door = 1
    # elif -40 <= x <= 40 and -60 <= y <= -40:
    #     #btn.clear()
    #     print("2 door")
    #     n_door = 2
    # elif 120 <= x <= 200 and -60 <= y <= -40:
    #     #btn.clear()
    #     print("3 door")
    #     n_door = 3
    # if -200 <= x <=-120 and 40 <= y <= 60:
    #     #btn.clear()
    #     print("1 door")
    #     n_door = 1
    # elif -40 <= x <= 40 and 40 <= y <= 60:
    #     #btn.clear()
    #     print("2 door")
    #     n_door = 2
    # elif 120 <= x <= 200 and 40 <= y <= 60:
    #     #btn.clear()
    #     print("3 door")
    #     n_door = 3
    # if -200 <= x <=-120 and 140 <= y <= 160:
    #     #btn.clear()
    #     print("1 door")
    #     n_door = 1
    # elif -40 <= x <= 40 and 140 <= y <= 160:
    #     #btn.clear()
    #     print("2 door")
    #     n_door = 2
    # elif 120 <= x <= 200 and 140 <= y <= 160:
    #     #btn.clear()
    #     print("3 door")
    #     n_door = 3   
    if -200 <= x <= -120 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("1 door")
        n_door = 1
    elif -40 <= x <= 40 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("2 door")
        n_door = 2
    elif 120 <= x <= 200 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("3 door")
        n_door = 3

    if n_door == ghost and n_door != 0:
        print("Попался!")
        n_floor = -1
        # t.color("#ff0000")
        ghost = randint(1, 3)
        print("ghost", ghost)
        what = False
        game(what)
    elif ghost != n_door and n_door != 0:
        n_floor -= 1
        delta_y += 120
        print("Вы перешли на другой уровень")
        t.width(3)
        t.color("#00ff00")
        ghost = randint(1, 3)
        print("ghost", ghost)
        if n_floor == -1:
            what = True
            game(what)

    if n_floor == 2:
        if n_door == 1:
            gt(t, -200, -60)
        elif n_door == 2:
            gt(t, -40, -60)
        elif n_door == 3:
            gt(t, 120, -60)
    elif n_floor == 1:
        if n_door == 1:
            gt(t, -200, 40)
        elif n_door == 2:
            gt(t, -40, 40)
        elif n_door == 3:
            gt(t, 120, 40)
    elif n_floor == 0:
        if n_door == 1:
            gt(t, -200, 140)
        elif n_door == 2:
            gt(t, -40, 140)
        elif n_door == 3:
            gt(t, 120, 140)

    # поскольку выше в функции get_pos() переменная n_floor глобально получает -1, то номера этажей на единичку меньше
    # когда проиграли или победили n_floor получает значение -1 и прямоугольники не отрисовываются
    if n_floor == 2 or n_floor == 1 or n_floor == 0:
        t.begin_fill()
        hatch()
        t.end_fill()

# drawing button 'start'
draw_button(-30, 5, 100, 30, 90)

# ПОКА НЕ НАЖАТА КЛАВИША '1' ИГРА НЕ НАЧНЕТСЯ
pause = True
while pause:
    w.update()
    turtle.listen()
    turtle.onkeypress(keyword_button_press, key=1) # обработка нажатой кнопки '1' . <<функция, кнопка>>

turtle.onkeypress(draw_stage_levels, key=2) # обработка нажатой кнопки '2' . <<функция, кнопка>>

turtle.listen()

# drawing landscape
draw_landscape()

# drawing hatches
draw_hatches()

# check position
t.screen.onclick(get_pos) # кри клике ЛКМ запуск функции qet_pos()

w.update() # нужно при включенном delay (обновление экрана) w.tracer(n=1, delay=5)
w.listen()
w.onkeypress(quit_game, "Escape") # при нажатии клавиши "Esc" запуск функции quit_game()
w.mainloop()