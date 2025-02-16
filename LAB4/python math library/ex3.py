import math

def apothem(length, sides):
    return length / (2 * math.tan(math.pi / sides))

def area(length, sides, a):
    return (length * a * sides) / 2

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side:"))
a = apothem(length, sides)

print("The area of the polygon is:", int(area(length, sides, a)))
