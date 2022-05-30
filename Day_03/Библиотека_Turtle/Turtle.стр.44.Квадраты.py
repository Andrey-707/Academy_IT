# Библиотека 'turtle' квадраты.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# первый квадрат
t.begin_fill()
for i in range(4):
    t.fd(150)
    t.left(90)
t.color("green")
t.end_fill()

# перемещение черепахи
t.color("black")
t.penup()
t.fd(-50)
t.left(90)
t.pendown()

# второй квадрат
t.begin_fill()
for i in range(4):
    t.fd(150)
    t.left(90)
t.color("red")
t.end_fill()

#s.mainloop() # цикл
s.exitonclick() # выход по клику
