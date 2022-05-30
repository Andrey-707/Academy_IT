# Библиотека 'turtle' буква 'В'
import turtle


# окно
s = turtle.Screen()
s.setup(600, 600)

# черепаха
t = turtle.Pen()
t.speed(1)
t.width(5)

n = 4

# верх
for i in range(n):
    t.fd(75)
    t.lt(360 / n)

# низ
t.rt(90)
for i in range(n):
    t.fd(75 * n/2)
    t.lt(360 / n)

#s.mainloop() # цикл
s.exitonclick() # выход по клику
