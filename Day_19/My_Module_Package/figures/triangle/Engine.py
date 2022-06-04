# Triangle Engine

from math import sqrt


def triangle_perimeter(default_a=7, default_b=2, default_c=8):
    '''Calculates the perimeter of a triangle'''
    x = default_a + default_b + default_c
    return round(x, 3)

def triangle_area(default_a=7, default_b=2, default_c=8):
    '''Calculates the area of a triangle'''
    p = (default_a + default_b + default_c) / 2
    x = sqrt(p * (p * (p - default_a) * (p - default_b) * (p - default_c)))
    return round(x, 3)


# run
if __name__ == "__main__":
    print(triangle_perimeter())
    print(triangle_area())
