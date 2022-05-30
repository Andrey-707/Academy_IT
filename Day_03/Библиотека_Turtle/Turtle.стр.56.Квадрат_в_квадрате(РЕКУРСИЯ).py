# Библиотека 'turtle' квадрат в квадрате (РЕКУРСИЯ).
import turtle


def immersion(x, y, step, deep=4):
    '''Рекурсивная функция рисования'''
    alpha = 20
    beta = 40
    if deep < 1:
        return
    x += step
    t.goto(x, y)
    y -= step
    t.goto(x, y)
    x -= step
    t.goto(x, y)
    y += step
    t.goto(x, y)
    step -= beta
    x += alpha
    y -= alpha
    t.penup()
    t.goto(x, y)
    t.pendown()
    immersion(x, y, step, deep-1)


# окно
s = turtle.Screen()
s.title("Square in square")
s.setup(600, 600)
s.bgcolor("black")

# черепаха
t = turtle.Pen()
t.color("white")
t.speed(1)
t.width(3)

# перемещение черепахи
t.penup()
t.goto(-75, 75)
t.pendown()

# run
immersion(-75, 75, 140)

# спрятать черепаху после отрисовки
t.hideturtle()

#s.mainloop() # цикл
s.exitonclick() # выход по клику
