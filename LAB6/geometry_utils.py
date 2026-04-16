import math

def circle_area(radius):
    if radius <= 0:
        print("Input Error: Radius must be positive.")
        return
    return math.pi * radius * radius, 2


def circle_perimeter(radius):
    if radius <= 0:
        print("Input Error: Radius must be positive.")
        return
    return 2 * math.pi * radius, 2


def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        print("Input Error: Dimensions must be strictly positive.")
        return
    return width * height


def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        print("Input Error: Dimensions must be strictly positive.")
        return
    return 2 * (width + height)


def triangle_area(base, height):
    if base <= 0 or height <= 0:
        print("Input Error: Dimensions must be strictly positive.")
        return
    return (base * height) / 2