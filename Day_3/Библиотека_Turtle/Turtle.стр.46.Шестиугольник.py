# Библиотека 'turtle' шестиугольник.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# шестиугольник
for i in range(6):
    t.fd(150)
    t.lt(60)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
