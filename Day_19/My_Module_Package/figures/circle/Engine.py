# Circle Engine

from math import pi


def circle_perimeter(default_radius=5):
    '''Calculates the perimeter of a circle'''
    x = 2 * pi * default_radius
    return round(x, 3)

def circle_area(default_radius=5):
    '''Calculates the area of a circle'''
    x = pi * default_radius ** 2
    return round(x, 3)


# run
if __name__ == "__main__":
	print(circle_perimeter())
	print(circle_area())
