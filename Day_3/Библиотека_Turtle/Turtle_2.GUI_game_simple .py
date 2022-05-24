# Библиотека 'turtle' 2.GUI_simple
import turtle


# окно/холст
s = turtle.Screen()
s.title("Circle game")
s.setup(500, 500)

# кнопка (button)
btn = turtle.Turtle()
btn.hideturtle()

# нарисовать кнопку
btn.setposition(-40, 0)
btn.begin_fill()
btn.fillcolor("green")
for i in range(2):
    btn.fd(80)
    btn.left(90)
    btn.fd(30)
    btn.left(90)
btn.end_fill()

# переместить перо и написать "Start"
btn.penup()
btn.goto(-17, 5)
btn.color("white") # устанавливает цвет линии
btn.write("Start", font=("Arial", 12, "normal"))

# круг (circle)
circ = turtle.Turtle()
circ.hideturtle()
circ.shape("circle")
circ.color("orange")

# квадрат (square)
sq = turtle.Turtle()
sq.hideturtle()
sq.penup()
sq.setposition(-20, 70)

def btnclick(x, y):
    '''Функция реагирует на попадание 'x' и 'y' в периметр кнопки Start'''
    if -40 < x < 40 and 0 < y < 30:
        btn.clear()
        circ.showturtle()
        circ.penup()
        sq.pendown()
        print("sq position:", sq.xcor(), sq.ycor())
        for i in range(4):
            sq.fd(40)
            sq.rt(90)

def up():
    '''Функция реагирует на покадание шарика в периметр квадрата'''
    y = circ.ycor() + 10
    circ.sety(y)
    if -20 < circ.xcor() < 20 and 30 < circ.ycor() < 70:
        circ.hideturtle()
        sq.clear()
        circ.setposition(-70, 0)
        circ.write("Game Over!", font=("Arial", 18, "bold"))


# прослушивает события холста
turtle.listen()

# событие нажатия клавиши
turtle.onscreenclick(btnclick, 1)

# событие нажатия клавиши
turtle.onkeypress(up, "Up")

# предотвращает закрытие холста
turtle.done()
