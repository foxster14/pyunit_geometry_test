import abc
import math

def perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def semiPerimeter(perimeter):
    semi_perimeter = perimeter / 2
    return semi_perimeter

def surfaceArea(s, side1, side2, side3):
    surface_area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return surface_area


def main():
    side1 = eval(input("Please enter the first side of a triangle: "))
    side2 = eval(input("Please enter the second side of a triangle: "))
    side3 = eval(input("Please enter the third side of a triangle: "))
    print()

    p = perimeter(side1, side2, side3)
    s = semiPerimeter(p)
    a = surfaceArea(s, side1, side2, side3)
    
    print("The perimeter of a triangle = ", float(p))
    print("The semi-perimeter of a triangle = ", s)
    print("The area of a triangle = ",round(a,2))

if __name__ == '__main__':
    main()