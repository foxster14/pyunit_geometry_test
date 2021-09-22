import sphere
import cylinder

def main():

    while True:
        print("Welcome to my Geometry Program")
        print("1. Sphere") ## menu goes here
        print("0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 0:
            break
        if selection == 1:
            sphere.main()

main()