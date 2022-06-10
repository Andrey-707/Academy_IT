# Модуль_fractions. Дроби.

from fractions import Fraction


print(Fraction(3, 9)) # OUT: 1/3

# тут показан недостаток Python (у числа отстается хвост)
print(0.1*3+0.1*3+0.1*3) # OUT: 0.9000000000000001

print(Fraction("1/3")) # OUT: 1/3

print(Fraction(3.25)) # OUT: 13/4

f = Fraction("1/3")
print(f+3, f*3, f+f, f + Fraction(str(0.2))) # OUT: 10/3 1 2/3 8/15

print(type(f+2)) # OUT: <class 'fractions.Fraction'>

print(float(f)) # OUT: 0.3333333333333333

f2 = Fraction('0.1')
print(f2*3 + f2*3 + f2*3) # OUT: 9/10

print(9**19) # OUT: 1350851717672992089

print(float(9**19)) # OUT: 1.350851717672992e+18

print(int(float(9**19))) # OUT: 1350851717672992000

print(9**19-int(float(9**19))) # OUT: 89
