import math

def main():
    base1 = int(input("Please Enter the Base1: "))
    base2 = int(input("Please Enter the Base2: "))
    height = int(input("Please Enter the Height: "))

    area = (base1 + base2)/2 * height
    median = 0.5 * (base1 + base2)
    print("\nArea of a Trapezoid =", area)
    print("Media of a Trapezoid =", median)

if __name__ == '__main__':
    main()