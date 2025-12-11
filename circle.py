import math


def area(r):
    """
    Calculates the area of a circle

        Params:
            r (int / float): The radius of the circle

        Result:
            area (float): The area of the circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of a circle

        Params:
            r (int / float): The radius of the circle

        Result:
            perimeter (float): The perimeter of the circle
    """
    return 2 * math.pi * r
