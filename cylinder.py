import math

def surfaceArea(radius, height):
    surfaceArea = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    return surfaceArea

def volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def lateral(radius, height):
    lateral = 2 * math.pi * radius * height
    return lateral

def base(radius):
    base = math.pi * radius**2
    return base

def main():
    radius = int(input("\nPlease enter the radius: "))
    height = int(input("Please enter the height: "))   

    print("The surface area of a cylinder =", round(surfaceArea(radius, height), 2))
    print("The volume of a cylinder =", round(volume(radius, height), 2))
    print("The lateral surface area of a cylinder =", round(lateral(radius, height), 2))
    print("The top OR bottom surface area of a cylinder =", round(base(radius), 2))

if __name__ == '__main__':
    main()
