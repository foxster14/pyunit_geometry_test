import math

def main():
    radius = int(input("\nPlease enter the radius: "))
    height = int(input("Please enter the height: "))
    
    surfaceArea = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    volume = math.pi * radius**2 * height
    lateral = 2 * math.pi * radius * height
    base = math.pi * radius**2

    print("The surface area of a cylinder =", round(surfaceArea, 2))
    print("The volume of a cylinder =", round(volume, 2))
    print("The lateral surface area of a cylinder =", round(lateral, 2))
    print("The top OR bottom surface area of a cylinder =", round(base, 2))

if __name__ == '__main__':
    main()
