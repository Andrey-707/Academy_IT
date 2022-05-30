# Библиотека 'turtle' паук.
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(2)

# паук
for i in range(12):
    t.fd(100)
    t.stamp()
    t.fd(-100)
    t.left(30)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
