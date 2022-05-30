# Библиотека 'turtle' квадратная спираль
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# квадратная спираль
for i in range(20):
    t.fd(i*10)
    t.lt(90)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
