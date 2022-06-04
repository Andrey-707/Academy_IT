# Задача№3.стр.29.Дата_и_время.Високосный_год.
# Преобразуйте класс Time в класс DataTime. Он должен хранить в себе информацию о дне, часа и минутах. Дни могут быть
# неограниченно большими, а так же орицательными. 
# Измените методы для сложения и вычитания так, чтобы они корректно складывали время и дни.

# Дополнительно: добавьте как можно больше методов перегрузки.
class Time:
    '''Class Time'''
    def __init__(self, D=0, h=0, m=0):
        '''Magic method. Initialization object'''

        # Абсолютное время храним в сек, поэтому переводим дни, часы в минуты
        total = D*1440 + h*60 + m
        self.D = total // (60 * 24)
        self.h = total // 60 % 24
        self.m = total % 60

    def __str__(self):
        '''Magic method. Return data in string format "##.d HH:MM" '''
        return f"{self.D:02}.d {self.h:02}:{self.m}"

    def __add__(self, other):
        '''Magic method. Add other to days, hours and minutes'''
        return Time(self.D + other.D, self.h + other.h, self.m + other.m)

    def __mul__(self, other):
        '''Magic method. Multiply days, hours and minutes by other'''
        if isinstance(other, int):
            return Time(self.D * other, self.h * other, self.m * other)

    def __sub__(self, other):
        '''Magic method. Subtract other from days, hours and minutes'''
        return Time(self.D - other.D, self.h - other.h, self.m - other.m)

    def __int__(self):
        '''Magic method. Converts days and hours to minutes'''
        return self.D*24*60 + self.h*60 + self.m

    def __lt__(self, other):
        '''Magic method. Compares values converted to minutes'''
        return int(self) < int(other)

    def __gt__(self, other):
        '''Magic method. Compares values converted to minutes'''
        return int(self) > int(other)

    def __eq__(self, other):
        '''Magic method. Equality values converted to minutes'''
        return int(self) == int(other)


# run
# Создаем экземпляр класса с именем 'my_time', который принимает значение 2 дня, 0 часов, 100 минут.
# В процессе инициализации происходит деление минут с остатком на % 60, поэтому в результате 40
my_time = Time(2, 0, 100)
print(my_time.D, my_time.h, my_time.m) # OUT: 2 1 40

# Добавим Magic method __str__, который отформатирует вывод времени на экран.
print(my_time) # OUT: 02.d 01:40

# Добавим Magic method __add__, который позволит добавить ко времени часы и минуты. Введем экземпляр
# класса Time в качестве переменной 'over_time' и добавим её значение времени к значению времени
# 'my_time' (т.е. +15 минут).
over_time = Time(0, 0, 15)
print(my_time + over_time) # OUT: 02.d 01:55

# Добавим Magic method __mul__, который позволит умножить время на значение переменной. Введем
# переменную-множитель и умножим значение времени 'over_time' (00:15) на значение переменной-множителя
# (т.е. удвоим).
mult = 2
print(over_time * 2) # OUT: 00.d 00:30

# Добавим Magic method __sub__, который позволит вычесть из времени часы и минуты. Введем экземпляр
# класса Time в качестве переменной 'cofee_time' и вычтем её значение времени из значения времени
# 'my_time' (т.е. -15 минут).
cofee_time = Time(0, 0, 15)
print(my_time - cofee_time) # OUT: 02.d 01:25

# Добавим Magic method __int__ (НЕ __init__), который преобразует текущее время 'my_time' к минутам.
# Т.е. мы получим то значение, которое мы вводили в самом начале программы (100 минут).
print(int(my_time)) # OUT: 2980

# Добавим Magic method __lt__, который сравнивает к примеру 'my_time' со значением 'cofee_time' (меньше).
print(my_time < cofee_time) # OUT: False

# Добавим Magic method __gt__, который сравнивает к примеру 'my_time' со значением 'cofee_time' (больше).
print(my_time > cofee_time) # OUT: True

# Добавим Magic method __eq__, который сравнивает к примеру 'my_time' со значением 'cofee_time' (равенство).
print(my_time == cofee_time) # OUT: False
