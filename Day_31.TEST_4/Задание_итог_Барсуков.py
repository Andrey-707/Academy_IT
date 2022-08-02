# Задание_итог_Барсуков
# СОРТИРОВКА МЕТОДОМ ПУЗЫРЬКА

from time import time
from random import randint
from rich import print


def bub_sort(A:list):
    """Data sorting function. Takes data type list"""
    N = len(A)
    for bypass in range(1, N):
        for i in range(0, N-bypass):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


def nask(amin:int=20, amax:int=1000):
    """Get input from user then check value for min and max"""
    if amin < 20: # check minimum argument
        amin = 20
    if amax > 1000: # check maximum argument
        amax = 1000
    flag = True
    while flag:
        try:
            a = int(input(f"Enter a number from {amin} to {amax}: "))
            if a < amin:
                print(f"[red]Entered value is less than {amin}[/]")
                raise ValueError ("Invalid value")
            elif a > amax:
                print(f"[red]Entered value is greater than {amax}[/]")
                raise ValueError ("Invalid value")
            else:
                print(f"[green]Entered value is in range from {amin} to {amax}[/]")
                flag = False # if no exceptions exit loop
        except Exception:
            print("[red]Error! Try again[/]")
    return a


# Create list (NO arguments)
list_A = [randint(10000 , 99999) for i in range(nask())]

# Create list (OK arguments)
# list_A = [randint(10000 , 99999) for i in range(nask(30, 900))]

# Create list (NOT OK arguments)
# list_A = [randint(10000 , 99999) for i in range(nask(5, 2000))]

# Number of numbers in list 'list_A'
numbers = len(list_A)
print(f"[yellow]\no Number of numbers in the 'list_A': {numbers}[/]")

# Unsorted list
print("\nUnsorted list:")
print(*list_A)

# Time spent sorting
start = time()
bub_sort(list_A)
finish = round(time() - start, 3)
print(f"[yellow]\no Processor time spent on sorting: {finish}[/]")

# Sorted list
print("\nBubble sorted list:")
print(*list_A)

# Sum of 10 maximum numbers
max_sum = sum(list_A[-1:-11:-1])
print(f"[yellow]\no Sum of 10 maximum numbers: {max_sum}[/]")

# Sum of 10 minimum numbers
min_sum = sum(list_A[0:10])
print(f"[yellow]\no Sum of 10 minimum numbers: {min_sum}[/]")
