# Библиотека 'turtle' бабочка.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(2)
t.width(3)

# бабочка
t.begin_fill()
for i in range(3):
    for i in range(3):
        t.fd(150)
        t.lt(120)
    t.lt(120)
t.color('yellow')
t.end_fill()

t.color('black')
t.lt(180)
for i in range(3):
    for i in range(3):
        t.fd(150)
        t.lt(120)
    t.lt(120)
    
#s.mainloop() # цикл
s.exitonclick() # выход по клику
