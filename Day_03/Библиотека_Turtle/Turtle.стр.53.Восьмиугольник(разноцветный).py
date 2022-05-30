# Библиотека 'turtle' восьмиугольник (разноцветный).
import turtle
import random


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(5)

# цвета
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'yellow', 'pink', 'brown']

# восьмиугольник (разноцветный) 10 циклов
for i in range(10):
    for j in range(8):
        t.color(random.choice(colors))
        t.fd(100)
        t.lt(45)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
