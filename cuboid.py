
def surface(length, width, height):
    surface = (2 * length * width) + (2 * length * height) + (2 * height * width)
    return surface

def volume(length, width, height):
    volume = length * width * height
    return volume

def lateral(length, width, height):
    lateral = 2 * (length + width) * height
    return lateral

def main():
    length = int(input("Please Enter the length: "))
    width = int(input("Please Enter the width: "))
    height = int(input("Please Enter the height: "))
    
    print("The Surface Area of a Cuboid = {0:0.2f}" .format(surface(length, width, height)))
    print("The Volume of a Cuboid = {0:0.2f}" .format(volume(length, width, height)))
    print("The Lateral Surface Area of a Cuboid = {0:0.2f}" .format(lateral(length, width, height)))

if __name__ == '__main__':
    main()