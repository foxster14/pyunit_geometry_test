import sphere
import cylinder
import cone
import cube
import triangle
import trapezoid
import cuboid


def header(string):
    line="-" * 55 
    print(line, "\nPYTHON PROGRAM TO FIND", string, "\n" + line)

def main():

    while True:
        print("\nWelcome to my Geometry Program")
        ## menu ##
        print("1. Sphere")
        print("2. Cylinder")
        print("3. Cone")
        print("4. Cube")
        print("5. Triangle") ## put equilateral in here too
        print("6. Trapezoid")
        print("7. Cuboid")
        print("0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 0:
            break
        elif selection == 1:
            header("VOLUME & SURFACE AREA OF SPHERE")
            sphere.main()
        elif selection == 2:
            header("VOLUME & SURFACE AREA OF CYLINDER")
            cylinder.main()
        elif selection == 3:
            header("VOLUME & SURFACE AREA OF CONE")
            cone.main()
        elif selection == 4:
            header("VOLUME & SURFACE AREA OF CUBE")
            cube.main()
        elif selection == 5:
            header("AREA & PERIMETER OF A TRIANGLE")
            triangle.main()
        elif selection == 6:
            header("AREA & MEDIAN OF A TRAPEZOID")
            trapezoid.main()
        elif selection == 7:
            header("VOLUME & SURFACE AREA OF CUBOID")
            cuboid.main()
        else:
            print("Invalid selection, please try again.")

main()