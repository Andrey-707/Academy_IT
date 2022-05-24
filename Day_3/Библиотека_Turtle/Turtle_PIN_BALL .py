import turtle, random, time


def btnclick(x, y):
    '''Функция реагирует на попадание "x" и "y" в периметр кнопки START'''
    global pause
    if -40 < x < 50 and 0 < y < 40:
        print("Кнопка нажата!")
        btn.clear()
        pause = False
        draw_frame()


def draw_button():
    '''Функция рисует кнопку START'''
    btn.setposition(-40, 0)
    btn.begin_fill()
    btn.fillcolor("green")
    for i in range(2):
        btn.fd(90)
        btn.left(90)
        btn.fd(40)
        btn.left(90)
    btn.end_fill()
    btn.penup()
    btn.goto(-25, 7)
    btn.color("white") # устанавливает цвет линии
    btn.write("START", font=("Arial", 12, "normal"))


def draw_frame():
    '''Функция рисует поле'''
    frame.begin_fill()
    frame.color("white")
    for i in range(4):
        frame.rt(90)
        frame.fd(400)
    frame.end_fill()


def draw_ball():
    '''Функция запускает мяч с рандомным ускорением по осям "x" и "y" '''
    ball.showturtle()
    delta_x = random.randint(2, 20)
    delta_y = random.randint(2, 20)
    while running:
        x, y = ball.position()
        if x + delta_x >= 196 or x + delta_x <= -198:
            delta_x = -delta_x
        if y + delta_y >= 200 or y + delta_y <= -198:
            delta_y = - delta_y
        ball.goto(x + delta_x, y + delta_y)


def message(text, color):
    '''Функция очищает холст, выводит сообщение'''
    global running
    running = False
    btn.hideturtle()
    btn.goto(-100, 0)
    btn.color(color)
    ball.clear()
    frame.clear()
    s.bgcolor("black")
    btn.write(text, font=("Arial", 18, "bold"))
    time.sleep(3)


def quit_game():
    '''Функция выхода из игры'''
    message(mes_txt, "red")
    s.bye()


# окно/холст
s = turtle.Screen()
s.setup(450, 450)
s.bgcolor("black")
s.title("Pin Ball") 

# кнопка
btn = turtle.Turtle()
btn.color("white")
btn.speed(0) # мгновенная отрисовка
btn.hideturtle()

# поле для мяча
frame = turtle.Turtle()
frame.speed(0) # мгновенная отрисовка
frame.hideturtle()
frame.penup()
frame.goto(197, 202)
frame.pendown()
frame.width(5)

# мяч
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()

# установить мяч
ball.hideturtle()
ball.goto(0, 198)

# message text
mes_txt = "GAME OVER"

# run
draw_button()

# ПОКА НЕ НАЖАТА КНОПКА 'START' ИГРА НЕ НАЧНЕТСЯ
pause = True
while pause:
    s.update()
    turtle.listen()
    turtle.onscreenclick(btnclick, 1)

# переменная цикла функции draw_ball
running = True

# событие нажатия клавиши
turtle.onkeypress(draw_ball, "space") # запускает мяч при нажатии "space"
s.onkeypress(quit_game, "Escape") # выходит изи игры при нажатии "Escape"

# прослушивает события холста
s.update()
turtle.listen()
s.listen()

# предотвращает закрытие холста
turtle.done()
