# Библиотека 'turtle' 3.GUI_advanced
import turtle


def prepare_fig(fig, x, y):
    '''Функция подготовки фигуры'''
    fig.hideturtle()
    fig.penup()
    fig.setposition(x, y)
    fig.speed(13)


def draw_square(fig, color, side_length):
    '''Функция отрисовки квадрата'''
    fig.pendown()
    fig.fillcolor(color)
    fig.begin_fill()
    for i in range(4):
        fig.fd(side_length)
        fig.rt(90)
    fig.end_fill()


def message(text, color):
    '''Функция сообщений'''
    circ.hideturtle()
    circ.goto(-100, 0)
    circ.color(color)
    sq.clear()
    sq2.clear()
    print(moves)
    s.bgcolor("black")
    circ.write(text, font=("Arial", 18, "bold"))


# def win_or_die(moves):
def die_or_alive(moves):
    '''Мертвый или живой'''
    if -20 < circ.xcor() < 40 and 10 < circ.ycor() < 70:
        s.bgcolor("black")
        message(GAME_OVER_MSG + str(moves), 'red')
    if -60 < circ.xcor() < -20 and 50 < circ.ycor() < 90:
        message(WIN_MSG + str(moves), 'green')
        circ.color("green")


def movey(deltay):
    '''Движение по оси y'''
    global moves
    y = circ.ycor() + deltay
    circ.sety(y)
    moves += 1
    die_or_alive(moves)


def movex(deltax):
    '''Движение по оси x'''
    global moves
    x = circ.xcor() + deltax
    circ.setx(x)
    moves += 1
    die_or_alive(moves)


# окно/холст
s = turtle.Screen()
s.title("Circle game")
s.setup(500, 500)

# круг (circle)
circ = turtle.Turtle()
circ.penup()
circ.shape("circle")
circ.color("orange")

# квадрат 1 (square)
sq = turtle.Turtle()
prepare_fig(sq, -20, 70)
draw_square(sq, "red", 60)

# квадрат 2 (square)
sq2 = turtle.Turtle()
prepare_fig(sq2, -60, 90)
draw_square(sq2, "green", 40)

# сделано ходов (при старте равно 0)
moves = 0

# if you die
GAME_OVER_MSG = "You died!\nMoves made: "

# if you alive
WIN_MSG = "You alive!\nMoves made: "

# величина шага
STEP = 10

# прослушивает события холста
turtle.listen()

# события нажатия клавиш
turtle.onkeypress(lambda: movey(STEP), 'Up')
turtle.onkeypress(lambda: movey(-STEP), 'Down')
turtle.onkeypress(lambda: movex(STEP), 'Right')
turtle.onkeypress(lambda: movex(-STEP), 'Left')

# предотвращает закрытие холста
turtle.done()
