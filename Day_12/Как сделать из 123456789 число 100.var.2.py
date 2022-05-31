# Задача№5.стр.30.
# У вас есть девять цифр 1,2, ..., 9. Именно в таком порядке вы можете вставлять между ними "+", "-" или ничего.
# У вас будут получаться выражения вида 123+45-6+7-89.
# Найдите все из них, которые равны 100.


from itertools import product, islice
from rich import print 
 
def expr(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)


def gen_expr():
    op = ['+', '-', ''] 
    return [expr(p) for p in product(op, repeat=9) if p[0] != '+']
 

def all_exprs():
    values = {}
    for expr in gen_expr():
        val = eval(expr)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values
 
 
def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
        print(s)
 
 
def max_solve():
    print("Sum {} has the maximum number of solutions: {}".
          format(*max(all_exprs().items(), key=lambda x: x[1])))
    
 
def min_solve():
    values = all_exprs()
    for i in range(123456789):
        if i not in values:
            print("Lowest positive sum that can't be expressed: {}".format(i))
            return
 
 
def highest_sums(n=10):
    sums = map(lambda x: x[0],
               islice(sorted(all_exprs().items(), key=lambda x: x[0], reverse=True), n))
    print("Highest Sums: {}".format(list(sums)))
 
 
sum_to(100)
max_solve()
min_solve()
highest_sums()