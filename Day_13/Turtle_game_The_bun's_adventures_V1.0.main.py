# Barsukov Andrey
# Turtle game The bun's adventures
# Барсуков Андрей
# Turtle игра Приключения колобка

'''
ПРАВИЛА ИГРЫ:

Игрок начинает с нижнего (STAGE 3) уровня подземелья, нужно выбраться на поверхность, открыв при это три люка
дилее упоминаются как двери. По пути на поверхность необходимо открывать двери так, чтобы не попасться призракам.
Призраки появляются рандомно за 1, 2 или 3 дверью уровня. Всего три призрака, как и три двери. Первый призрак
появляется когда начинается игра, второй призрак появляется когда игрок переходит на уровень выше (STAGE 2) и 
последний призрак появляется, когда игрок переходит на уровень STAGE 1. Когда игрок откроет все три двери,
необходимо выбраться на поверхность (на игрове поле голубого цвета) и нажать кнопку, которой игрок до этого
открывал двери.

УПРАВЛЕНИЕ:

mouse
left mouse button - выбрать позицию (открыть дверь)

Можно играть мышкой, выбирать двери снизу вверх, в конце кликнуть мышкой на верхний край игрового поля в то
место, если бы двери отрисовались на уровень выше (например, на верх солнышка). Если игрок нажал в нужное место,
игра сообщит о победе.

keyboard
'left' - движение влево
'right' - движение вараво
'up' - движение вверх
'down' - движение вниз
'1' - запустить отрисовку карты когда игра на стартовой заставке (снять с паузы). Стирает название уровней
'2' - добавляет название уровней на игровое поле
'space' - выбрать позицию (открыть дверь)
'escape' - выйти из игры

Можно управлять колобком стрелками (вверх, вниз, влево и вправо), кнопкой 'SPACE' открывать двери, на поверхности
(на игровом поле голубого цвета) нажать кнопку 'SPACE' чтобы победить. Чтобы выйти из игры нужно победить,
проиграть или нажать кнопку 'Escape'.
'''

import turtle
import time

from random import randint


def gt(turtle, x, y):
    '''Puts turtle on x and y coords'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def movex(deltax):
    '''Checks x coords'''
    # global moves # for counting movements
    x = b.xcor() + deltax
    b.setx(x)
    # moves += 1 # for counting movements

def movey(deltay):
    '''Checks y coords'''
    # global moves # for counting movements
    y = b.ycor() + deltay
    b.sety(y)
    # moves += 1 # for counting movements

def draw_button(x, y):
    '''Draws "start" button '''
    gt(btn, x, y)
    btn.begin_fill()
    rect(btn, 180, 30, 90)
    btn.fillcolor("black")
    btn.end_fill()
    gt(btn, x+15, y+2)
    btn.pencolor("white")
    btn.write("Press 1 to start", font=("Arial", 12, "bold"))
    btn.hideturtle()

def rect(turtle, x, y, angle):
    '''Draws rectangle'''
    for i in range(2):
        turtle.fd(x)
        turtle.lt(angle)
        turtle.fd(y)
        turtle.lt(angle)

def keyword_button_press():
    '''If button "1" pressed removes all 'btn' (btn = turtle.Turtle()) captions'''
    global pause
    # print("Button '1' pressed")
    btn.clear()
    pause = False

def draw_landscape():
    '''Draws landscape'''
    
    # Earth/Земля
    t.color("black")
    gt(t, -250, -250)
    t.begin_fill()
    rect(t, 500, 100, 90)
    t.fillcolor("black")
    t.end_fill()

    # Sky/небо
    gt(t, -250, 150)
    t.begin_fill()
    rect(t, 500, 100, 90)
    t.fillcolor("#285078") # clear sky color
    t.end_fill()

    # Sun/Солнце (круг)
    t.color("black")
    gt(t, 200, 200)
    t.fillcolor("Yellow")
    t.begin_fill()
    for i in range(180):
        t.fd(1)
        t.lt(2)
    t.end_fill()
    # Sunbeam/Солнечный луч 1
    t.lt(180)
    gt(t, 160, 235)
    t.begin_fill()
    rect(t, 20, 4, 90)
    t.fillcolor("Yellow")
    t.end_fill()
    # Sunbeam/Солнечный луч 2
    t.lt(30)
    gt(t, 165, 210)
    t.begin_fill()
    rect(t, 20, 4, 90)
    t.fillcolor("Yellow")
    t.end_fill()
    # Sunbeam/Солнечный луч 3
    gt(t, 187, 193)
    t.begin_fill()
    t.lt(30)
    rect(t, 20, 4, 90)
    t.fillcolor("Yellow")
    t.end_fill()
    # Sunbeam/Солнечный луч 4
    t.lt(30)
    gt(t, 215, 193)
    t.begin_fill()
    rect(t, 20, 4, 90)
    t.fillcolor("Yellow")
    t.end_fill()

    # Upper bound/Верхняя граница
    t.lt(90)
    gt(t, -250, 50)
    t.fd(500)
    # Lower bound/Нижняя граница
    gt(t, -250, -50)
    t.fd(500)

    # Dungeon levels/Уровни подземелий
    btn.color("black")
    gt(btn, 0, 80)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья
    gt(btn, 0, -20)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья
    gt(btn, 0, -125)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold")) # обозначение уровней подземелья

def draw_hatches():
    '''Draws game field'''

    # Upper level/Верхний уровень
    # hatch/люк 1
    t.color("black")
    gt(t, -200, 140)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 2
    gt(t, -40, 140)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 3
    gt(t, 120, 140)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()

    # Middle level/Средний уровень
    # hatch/люк 1
    gt(t, -200, 40)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 2
    gt(t, -40, 40)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 3
    gt(t, 120, 40)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()

    # Lower level/Нижний уровень
    # hatch/люк 1
    gt(t, -200, -60)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 2
    gt(t, -40, -60)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()
    # hatch/люк 3
    gt(t, 120, -60)
    t.begin_fill()
    rect(t, 80, 20, 90)
    t.end_fill()

def draw_dungeon_levels():
    '''Draws dungeon levels'''
    # print("Button '2' pressed")
    btn.color("black")
    gt(btn, 0, 80)
    btn.write("STAGE_1", align="center", font = ("Courier", 12, "bold"))
    gt(btn, 0, -20)
    btn.write("STAGE_2", align="center", font = ("Courier", 12, "bold"))
    gt(btn, 0, -125)
    btn.write("STAGE_3", align="center", font = ("Courier", 12, "bold"))
    btn.color('white')
    gt(btn, -220, -105)

def win_or_loose(what):
    '''Checks win of loose'''
    if what == True:
        w.clear()
        w.bgcolor("black")
        gt(t, -120, 0)
        t.color("green")
        t.write("YOU WIN", font=("Courier", 30, "bold"))
        time.sleep(5)
        quit_game()
    elif what == False:
        w.clear()
        w.bgcolor("red")
        gt(t, -170, 0)
        t.color("black")
        t.write("GOT CAUGTH", font=("Courier", 35, "bold"))
        time.sleep(5)
        quit_game()

def quit_game():
    '''Exits from the game'''
    w.clear()
    w.bgcolor("black")
    gt(t, -125, 0)
    if what:
        t.color("green")
    else:
        t.color("red")
    t.write("GAME OVER", font=("Courier", 25, "bold"))
    time.sleep(3)
    w.bye()

def check_ball_pos():
    '''Checks ball's positions'''
    global n_floor, ghost, what, delta_y
    # print(x, y, n_floor) # when testing
    n_door = 0
    x = b.xcor()
    y = b.ycor()
    if -200 <= x <= 200 and y > 160:
        n_floor = -1
        gt(btn, -100, 200)
        btn.color("white")
        b_coords = b.position()
        if b_coords[0] > 100:
            gt(btn, b_coords[0]-250, b_coords[1]+20)
        else:
            gt(btn, b_coords[0]-50, b_coords[1]+20)
        btn.write("It seems I got out!", font=("Courier", 10, "bold"))
        time.sleep(8)
        what = True
        win_or_loose(what)

    # ------ ИНТЕРВАЛ КООРДИНАТ ДЛЯ ПОЛУЧЕНИЯ n_door ПО Y ОТ _ И ДО _ (-60 -40; 40 60; 140 160) -----
    # по скольку разница в шаге по оси Y составляет 120, значение delta_y добавляется к координатам Y
    if -200 <= x <= -120 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        print("You 1")
        n_door = 1
    elif -40 <= x <= 40 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        print("You 2")
        n_door = 2
    elif 120 <= x <= 200 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("You 3")
        n_door = 3

    if n_door == ghost and n_door != 0:
        print("Ghost catch you!")
        what = False
        win_or_loose(what)
    elif n_door != ghost and n_door != 0:
        n_floor -= 1
        delta_y += 120
        print(f"You go to 'STAGE_{n_floor}'")
        if n_floor != 0:
            ghost = randint(1, 3)
            print("Ghost", ghost)
        else:
            ghost = None

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

    # Поскольку выше в функции check_ball_pos() переменная n_floor глобально получает -1, то номера этажей на единичку
    # меньше. Когда проиграли или победили n_floor получает значение -1 и прямоугольники не отрисовываются
    if n_floor == 2 or n_floor == 1 or n_floor == 0:
        t.begin_fill()
        rect(t, 80, 20, 90)
        t.fillcolor("forestgreen")
        t.end_fill()

def get_pos(x, y):
    '''Get position'''
    global n_floor, ghost, what, delta_y
    # print(x, y, n_floor) # when testing
    n_door = 0
    # ------ ИНТЕРВАЛ КООРДИНАТ ДЛЯ ПОЛУЧЕНИЯ n_door ПО Y ОТ _ И ДО _ (-60 -40; 40 60; 140 160) -----
    # по скольку разница в шаге по оси Y составляет 120, значение delta_y добавляется к координатам Y
    if -200 <= x <= -120 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("You 1")
        n_door = 1
    elif -40 <= x <= 40 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("You 2")
        n_door = 2
    elif 120 <= x <= 200 and 20*(n_floor-1) - 100 + delta_y <= y <= 20*(n_floor-1) - 80 + delta_y:
        btn.clear()
        print("You 3")
        n_door = 3

    if n_door == ghost and n_door != 0:
        print("Ghost catch you!")
        n_floor = -1
        what = False
        win_or_loose(what)
    elif ghost != n_door and n_door != 0:
        n_floor -= 1
        delta_y += 120
        print(f"You go to 'STAGE_{n_floor}'")
        t.width(3)
        if n_floor > 0:
            ghost = randint(1, 3)
            print("Ghost", ghost)
        elif n_floor == 0:
            ghost = None
        if n_floor == -1:
            what = True
            win_or_loose(what)

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

    # Поскольку выше в функции get_pos() переменная n_floor глобально получает -1, то номера этажей на единичку меньше.
    # Когда проиграли или победили n_floor получает значение -1 и прямоугольники не отрисовываются.
    if n_floor == 2 or n_floor == 1 or n_floor == 0:
        t.begin_fill()
        rect(t, 80, 20, 90)
        t.fillcolor("forestgreen")
        t.end_fill()

def game():
    '''Prepare game'''
    global w, t, btn, b, ghost, n_floor, delta_y, pause
    w = turtle.Screen()
    w.title("Game 'The bun's adventures'")
    w.setup(500, 500)
    # w.tracer(n=1, delay=5) # при delay=5 медленная отрисовка игрового поля
    w.tracer(n=1, delay=0) # при delay=0 мгновенная отрисовка игрового поля
    w.bgcolor("forestgreen")

    # This is because the turtle module (most reference implementations as of today) uses a class
    # variable called _RUNNING
    turtle.TurtleScreen._RUNNING = True

    # turtle
    t = turtle.Turtle()
    t.width(3)
    t.speed(10)
    t.shape("turtle")
    t.hideturtle()

    # button-turtle
    btn = turtle.Turtle()
    btn.color("white")
    btn.width(1)
    btn.hideturtle()

    # ball
    b = turtle.Turtle()
    b.hideturtle()
    b.penup()
    b.goto(-160, -120)
    b.shape("circle")
    b.color("orange")

    # assign exit from the game to a key 'Esc'
    w.onkeypress(quit_game, "Escape") # при нажатии клавиши "Esc" запуск функции quit_game()

    # drawing button 'start'
    draw_button(-95, 0)

    # start options
    n_floor = 3
    what = None
    delta_y = 0
    pause = True

    # press '1' to start game / ДЛЯ НАЧАЛА ИГРЫ НАЖАТЬ КЛАВИШУ '1'
    while pause:
        # если не установить "Выполнить обновление экрана черепахи", в этом месте программа повиснет
        w.update()
        turtle.onkeypress(keyword_button_press, key=1) # обработка нажатой кнопки '1' . <<функция, кнопка>>

    turtle.onkeypress(draw_dungeon_levels, key=2) # обработка нажатой кнопки '2' . <<функция, кнопка>>

    # start ghost position
    ghost = randint(1, 3)
    print("Ghost", ghost)

    # drawing landscape
    draw_landscape()

    # drawing hatches
    draw_hatches()

    # check position
    t.screen.onclick(get_pos) # кри клике ЛКМ запуск функции get_pos()

    # show ball
    b.showturtle()
    time.sleep(2)
    btn.clear()
    btn.color("white")
    gt(btn, -220, -105)
    btn.write("This is a bad place,\nI need to get out immediately !", font=("Courier", 10, "bold"))
    time.sleep(5)
    btn.clear()

    # ball's step
    step = 10

    # control
    turtle.onkeypress(lambda: movey(step), "Up")
    turtle.onkeypress(lambda: movey(-step), "Down")
    turtle.onkeypress(lambda: movex(step), "Right")
    turtle.onkeypress(lambda: movex(-step), "Left")
    turtle.onkeypress(check_ball_pos, "space")


# RUN GAME
if __name__ == "__main__":
    # если не установить ожидание черепахе, программа будте висеть в паузе и не отреагирует на нажатие '1'
    turtle.listen()
    game()
    w.mainloop()
