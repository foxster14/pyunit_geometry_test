def main():
    length = int(input("Please Enter the length: "))
    width = int(input("Please Enter the width: "))
    height = int(input("Please Enter the height: "))
    surface = (2 * length * width) + (2 * length * height) + (2 * height * width)
    volume = length * width * height
    lateral = 2 * (length + width) * height
    print("The Surface Area of a Cuboid = {0:0.2f}" .format(surface))
    print("The Volume of a Cuboid = {0:0.2f}" .format(volume))
    print("The Lateral Surface Area of a Cuboid = {0:0.2f}" .format(lateral))

if __name__ == '__main__':
    main()