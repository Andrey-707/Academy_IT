# Библиотека 'turtle' треугольник.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# треугольник
for i in range(3):
    t.fd(150)
    t.lt(120)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
