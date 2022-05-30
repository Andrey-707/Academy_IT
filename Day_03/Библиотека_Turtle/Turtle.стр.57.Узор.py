# Библиотека 'turtle' узор
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.width(2)
t.speed(10)

# узор
for i in range(10):
    for i in range(8):
        t.fd(80)
        t.lt(45)
    t.rt(36)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
