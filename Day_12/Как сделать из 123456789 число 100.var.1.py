# Задача№5.стр.30.
# У вас есть девять цифр 1,2, ..., 9. Именно в таком порядке вы можете вставлять между ними "+", "-" или ничего.
# У вас будут получаться выражения вида 123+45-6+7-89.
# Найдите все из них, которые равны 100.


from rich import print
from future import *
 
s = '123456789'
d = {'0':'', '1':'+', '2':'-'}
sum_num = 100
count =  0
 
def to_new_base(n, new_base):
    s = []
    if n == 0:
        s.append('0')
    while n:
        s.append(str(n % new_base))
        n = n // new_base
    num = '{0:0>8}'.format(''.join(s[::-1]))
    return num
 
 
for n in range(int('44444444', 5)):
    num = to_new_base(n, 3)
    expr = ''
    for i, j in zip(s, num):
        expr += i + d[j]
    expr += '9'
    if eval(expr) == sum_num:
        print('{0} = {1}'.format(expr, sum_num))
        count += 1

print('So, {0} expressions for {1}'.format(count, sum_num))