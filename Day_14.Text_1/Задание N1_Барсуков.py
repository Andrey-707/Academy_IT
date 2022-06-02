# Задание N1_Барсуков

#################################################################
## Solution of a quadratic equation << a*x**2 + b*x + c = 0 >> ##
#################################################################

def quadratic_equation(a:float, b:float, c:float):
    '''Function finds the roots of a quadratic equation << a*x**2 + b*x + c = 0 >> '''
    assert a != 0, "Уравнение cчитается квадратным при 'a' не равном нулю"
    # search for discriminant
    discr = b**2 - 4*a*c
    # search for roots
    if discr > 0:
        x1 = (-b-discr**(0.5)) / (2*a)
        x2 = (-b+discr**(0.5)) / (2*a)
        return round(x1, 5), round(x2, 5)
    # search for a single root
    elif discr == 0:
        x = -b / (2*a)
        return round(x, 5)
    # the equation has no roots (None)
    else:
        pass


################
## SINGLE RUN ##
################

# programm finds the roots once
try:
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    a, b, c = float(a), float(b), float(c)

    result = quadratic_equation(a, b, c)

    if isinstance(result, tuple):
        ft_root, sd_root = result
        print("Квадратное уравнение имеет два корня: " + str(ft_root) + " и " + str(sd_root))
    elif isinstance(result, float):
        print("Квадратное уравнение имеет один корень: " + str(result))
    else:
        print("Квадратное уравнение не имеет корней.")

except ValueError:
    print("ValueError! Input number.")
except AssertionError as a_ex:
    print("AssertionError!", a_ex)

##########
## LOOP ##
##########

# # programm finds the roots while flag
# flag = True
# while flag:
#     try:
#         cont = input("Continue y/n: ")
#         if cont == "y":
#             a = input("a = ")
#             b = input("b = ")
#             c = input("c = ")
#             a, b, c = float(a), float(b), float(c)

#             result = quadratic_equation(a, b, c)

#             if isinstance(result, tuple):
#                 ft_root, sd_root = result
#                 print("Квадратное уравнение имеет два корня: " + str(ft_root) + " и " + str(sd_root))
#             elif isinstance(result, float):
#                 print("Квадратное уравнение имеет один корень: " + str(result))
#             else:
#                 print("Квадратное уравнение не имеет корней.")

#         elif cont == "n":
#             print("Exit")
#             flag = False
#         else:
#             print("Incorrect input. Input y/n")
#     except ValueError:
#         print("ValueError. Input number.")
#     except AssertionError as a_ex:
#         print("AssertionError!", a_ex)
