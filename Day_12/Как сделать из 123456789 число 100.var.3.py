# Задача№5.стр.30.
# У вас есть девять цифр 1,2, ..., 9. Именно в таком порядке вы можете вставлять между ними "+", "-" или ничего.
# У вас будут получаться выражения вида 123+45-6+7-89.
# Найдите все из них, которые равны 100.

import time
from rich import print 
from operator import *
from itertools import *

start = time.time()
# дана стока чисел от 1 до 9
nums = "123456789"
print(nums)

# при помощи генератора из строки сделаем список чисел (int)
list_of_nums = [int(i) for i in nums]
print(list_of_nums)

for x in product(range(3), repeat=8):
    s = 0
    op = add
    num = list_of_nums[0]
    for i, a in enumerate(x):
        if a == 0:
            num = num*10 + list_of_nums[i+1]
        if a == 1:
            s = op(s, num)
            op = add
            num = list_of_nums[i+1]
        if a == 2:
            s = op(s, num)
            op = sub
            num = list_of_nums[i+1]
    s = op(s, num)
    if s == 100:
        print(list_of_nums[0], end="")
        for i, kod in enumerate(x, 1):
            if kod == 1:
                print(" + ",end="")
            if kod == 2:
                print(" – ",end="")
            print(list_of_nums[i],end="")
        print(" = 100")
print("Время: ", time.time() - start)