import math

def area(base1, base2, height):
    area = (base1 + base2)/2 * height
    return area

def median(base1, base2):
    median = 0.5 * (base1 + base2)
    return median

def main():
    base1 = int(input("Please Enter the Base1: "))
    base2 = int(input("Please Enter the Base2: "))
    height = int(input("Please Enter the Height: "))

    print("\nArea of a Trapezoid =", area(base1, base2, height))
    print("Media of a Trapezoid =", median(base1, base2))

if __name__ == '__main__':
    main()