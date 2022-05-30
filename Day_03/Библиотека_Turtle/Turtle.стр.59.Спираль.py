# Библиотека 'turtle' спираль
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(15)
t.width(2)

# спираль
for i in range(60):
    t.fd(i/2)
    t.lt(20)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
