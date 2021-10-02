import math


def main():
    radius = int(input("Please Enter the Radius of a Cone: "))
    height = int(input("Please Enter the Height of a Cone: "))

    slant = math.sqrt(radius**2 + height**2)
    surfaceArea = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))
    volume = math.pi * radius**2 * (height/3)
    lateral = math.pi * radius * math.sqrt(height**2 + radius**2)

    print("\nLength of a Side (slant) of a Cone =", round(slant,2))
    print("The Surface Area of a Cone =", round(surfaceArea,2))
    print("The Volume of a Cone =", round(volume,2))
    print("The Lateral Surface Area of a Cone =", round(lateral,2))

if __name__ == '__main__':
    main()
