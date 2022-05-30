# Библиотека 'turtle' квадрат в квадрате (координаты).
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# 
x = 0
y = 0
step = 150

# квадрат в квадрате
for i in range(4):
    x += step
    t.goto(x, y)
    y -= step
    t.goto(x, y)
    x -= step
    t.goto(x, y)
    y += step
    t.goto(x, y)
    # смещение внутрь
    step -= 20
    x += 10
    y -= 10
    t.penup()
    t.goto(x, y)
    t.pendown()

# спрятать черепаху после отрисовки
t.hideturtle()

#s.mainloop() # цикл
s.exitonclick() # выход по клику
