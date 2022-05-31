# Задача№5.стр.30.
# У вас есть девять цифр 1,2, ..., 9. Именно в таком порядке вы можете вставлять между ними "+", "-" или ничего.
# У вас будут получаться выражения вида 123+45-6+7-89.
# Найдите все из них, которые равны 100.

from rich import print 


# словарь для приведения к 16 ричной системе счисления
hex_dic = {0: "0", 1: "1", 2: "2", 3: "3",
           4: "4", 5: "5", 6: "6", 7: "7",
           8: "8", 9: "9",10: "a", 11: "b",
           12: "c", 13: "d", 14: "e", 15: "f", 16: "j"}

def convert(n1, n2, s):
    '''Функция конвертирует число 's' из 'n1' в 'n2' системы счисления'''
    s10 = int(s, n1)
    if n2 == 10:
        return s10
    l = [s10]
    i = 0
    while l[i] > (n2-1):
        a = l[i] % n2
        b = (l[i] - a) // n2
        l.append(b)
        l[i] = a
        i += 1
    s2 = ""
    for j in range(len(l)-1, 0-1, -1):
        s2 += hex_dic[l[j]]
    return s2

# словарь возможных символов, добавляемых между числами
sym_dic = {'0': "", '1': " - ", '2': " + "}



# дана стока чисел от 1 до 9
nums = "1 2 3 4 5 6 7 8 9"

# из строки сделаем список чисел (int)
list_of_nums = [int(i) for i in nums.split(" ")]

# входные данные
print("Входные данные:")
print(*list_of_nums)

def equal_to(L:list):
    '''Функция принимает список чисел и выдает возможные варианты решений по средствам функций print()'''
    global k, count
    k = 0 # переменная-счетчик числа итераций
    count = 0 # переменная-счетчик возможных вариантов решения задачи
    for i in range(3 ** 8):
        k += 1
        i_3 = convert(10, 3, str(i))
        l_symbol = ['0'] * (8 - len(i_3)) + list(i_3)
        combin = 0
        pr_oper = "+"
        num = L[0]

        for i_sym, sym in enumerate(l_symbol):
            if sym == '0':
                num = int(str(num) + str(L[i_sym + 1]))
            elif sym == '1':
                if pr_oper == "+":
                    combin += num
                elif pr_oper == "-":
                    combin -= num
                pr_oper = "-"
                num = L[i_sym + 1]
            elif sym == '2':
                if pr_oper == "+":
                    combin += num
                elif pr_oper == "-":
                    combin -= num
                pr_oper = "+"
                num = L[i_sym + 1]
        if pr_oper == "+":
            combin += num
        elif pr_oper == "-":
            combin -= num

        if combin == 100:
            print(f"1{sym_dic[l_symbol[0]]}2{sym_dic[l_symbol[1]]}3{sym_dic[l_symbol[2]]}"
                  f"4{sym_dic[l_symbol[3]]}5{sym_dic[l_symbol[4]]}6{sym_dic[l_symbol[5]]}"
                  f"7{sym_dic[l_symbol[6]]}8{sym_dic[l_symbol[7]]}9 = {combin}")
            count += 1

# выходные данные
print("\nВозможные комбинации для числа 100:")
# вызываем функцию и передаем в нее список чисел (int)
equal_to(list_of_nums)

print("\nКол-во итераций:", k)
# когда выполняется условие (в сумме получаем цифру 100), срабатывает переменная счетчик
print("Кол-во решений:", count)
