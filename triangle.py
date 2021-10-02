import math

def main():
    side_a = eval(input("Please enter the first side of a triangle: "))
    side_b = eval(input("Please enter the second side of a triangle: "))
    side_c = eval(input("Please enter the third side of a triangle: "))
    print()
    #
    perimeter = float(side_a + side_b + side_c)
    semi_perimeter = perimeter / 2
    s = semi_perimeter # Temp value
    surface_area = float(math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c)))
    #
    print("The perimeter of a triangle = ",perimeter)
    print("The semi-perimeter of a triangle = ", semi_perimeter)
    print("The area of a triangle = ",round(surface_area,2))

if __name__ == '__main__':
    main()