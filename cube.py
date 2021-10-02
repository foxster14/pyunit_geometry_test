import math

def surfaceArea(length):
    surface = 6.0 * length**2
    return surface

def volume(length):
    volume = length**3
    return volume

def lateralSurfaceArea(length):
    lateral = 4.0 * length**2
    return lateral

def main():
    length = int(input("Please Enter the Length of any Side of a Cube: "))
    print("\nSurface Area of Cube = {0:0.2f}" .format(surfaceArea(length)))
    print("Volume of Cube = {0:0.2f}" .format(volume(length)))
    print("Lateral Surface Area of Cube = {0:0.2f}" .format(lateralSurfaceArea(length)))

if __name__ == '__main__':
    main()
