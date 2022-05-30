# Библиотека 'turtle' звезда
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.width(2)
t.speed(1)

# звезда
for i in range(5):
    t.fd(200)
    t.rt(144)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
