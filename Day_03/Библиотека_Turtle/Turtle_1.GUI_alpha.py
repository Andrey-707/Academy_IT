# Библиотека 'turtle' 1.GUI_alpha
import turtle


# окно/холст
s = turtle.Screen()
s.title("Screen & Button")
s.setup(500, 500)

# кнопка
btn = turtle.Turtle()
btn.hideturtle()

# нарисовать кнопку
btn.begin_fill()
btn.fillcolor("green")
for i in range(2):
    btn.fd(100)
    btn.left(90)
    btn.fd(40)
    btn.left(90)
btn.end_fill()

# переместить перо и написать "BUTTON"
btn.penup()
btn.goto(11, 7)
btn.color("white") # устанавливает цвет линии
btn.write("BUTTON", font=("Arial", 12, "normal"))

def btnclick(x, y):
    '''Функция реагирует на попадание 'x' и 'y' в периметр кнопки Start'''
    if 0 < x < 100 and 0 < y < 40:
        print("Кнопка нажата!")
        btn.clear()
        ball = turtle.Turtle()
        turtle.fillcolor("orange")
        turtle.pencolor("purple")
        turtle.shape("circle")


# прослушивает события холста
turtle.listen()

# событие нажатия клавиши
turtle.onscreenclick(btnclick, 1)

# предотвращает закрытие холста
turtle.done()
