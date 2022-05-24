# Библиотека 'turtle' цветок.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(15)
t.width(2)

# цветок
for i in range(6):
    for j in range(360):
        t.fd(1)
        t.lt(1)
    t.rt(60)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
