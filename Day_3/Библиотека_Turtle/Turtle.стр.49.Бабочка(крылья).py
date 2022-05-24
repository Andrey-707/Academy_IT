# Библиотека 'turtle' бабочка (крылья).
import turtle

# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(3)
t.width(3)

# правое крыло
t.rt(90)
for q in range(10, 2-1, -2):
    for i in range(36):
        t.lt(10)
        t.fd(q)

# левое крыло
t.rt(190)
for q in range(10, 2-1, -2):
    for i in range(36):
        t.lt(10)
        t.fd(q)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
