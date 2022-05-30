# Библиотека 'turtle' круг. Тест скорости.
import turtle
import time


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.width(2)

# круг 1 скорость 1
t.speed(1)
start = time.time()
for i in range(360):
    t.fd(1)
    t.lt(1)
print(time.time() - start) # OUT: 11.475000143051147

# перемещение черепахи
t.penup()
t.fd(-50)
t.pendown()

# круг 2 скорость 15
t.speed(15)
start = time.time()
for i in range(360):
    t.fd(1)
    t.lt(1)
print(time.time() - start) # OUT: 8.17199993133545

#s.mainloop() # цикл
s.exitonclick() # выход по клику
