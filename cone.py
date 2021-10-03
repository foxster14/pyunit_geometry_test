import math

def slant(radius, height):
    slant = math.sqrt(radius**2 + height**2)
    return slant

def surface(radius, height):
    surfaceArea = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))
    return surfaceArea

def volume(radius, height):
    volume = math.pi * radius**2 * (height/3)
    return volume

def lateral(radius, height):
    lateral = math.pi * radius * math.sqrt(height**2 + radius**2)
    return lateral

def main():
    radius = int(input("Please Enter the Radius of a Cone: "))
    height = int(input("Please Enter the Height of a Cone: "))

    print("\nLength of a Side (slant) of a Cone =", round(slant(radius, height),2))
    print("The Surface Area of a Cone =", round(surface(radius, height),2))
    print("The Volume of a Cone =", round(volume(radius, height),2))
    print("The Lateral Surface Area of a Cone =", round(lateral(radius, height),2))

if __name__ == '__main__':
    main()
