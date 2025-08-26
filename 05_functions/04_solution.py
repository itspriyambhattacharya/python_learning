import math


def circle(rad):
    area = math.pi*rad**2
    circumference = 2*math.pi*rad
    return (area, circumference)


a, c = circle(4)
print(f"Area is: {a}\nCircumference is: {c}")
