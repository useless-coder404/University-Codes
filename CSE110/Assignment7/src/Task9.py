from math import pi


def area_circumference_generator(radius):
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return (area, circumference)


radius = float(input())
print(area_circumference_generator(radius))

area, circumference = area_circumference_generator(radius)
print(f"Area of the circle is {area} and circumference is {circumference}")
