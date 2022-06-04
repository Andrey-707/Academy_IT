# Square Engine


def square_perimeter(default_a=10):
    '''Calculates the perimeter of a square'''
    x = default_a * 4
    return round(x, 3)

def square_area(default_a=10):
    '''Calculates the area of a square'''
    x = default_a ** 2
    return round(x, 3)


# run
if __name__ == "__main__":
	print(square_perimeter())
	print(square_area())
