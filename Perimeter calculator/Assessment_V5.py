# Area and Perimeter calculator
# Date: 12/9/18
# Author: Aaron Heald
# Version 1: Basic setup with printing of decimals
# Version 2: Allow shorter inputs such as "a" and "p"
# Version 3: Allows the use of decimal numbers to be inputted
# Version 4: Print answers in cm + refinements
# Version 5: Allows Area and Perimeter to be done at once not separate

import math

# sets up the intcheck function
def intcheck(question):
        global response
        valid = False

        while not valid:
            response = input(question)
            try:
                response = float(response)
                if response > 150:
                    print("Can't Be Higher Then 150!")
                elif response <= 0:
                    print("Measurements can't be less than or equal to 0!")
                else:
                    print()
                    valid = True
            except ValueError:
                print("Please enter an number (decimal/integer)")
                print()
        return response


# sets up the strcheck function
def strcheck(question):
        global response
        valid = False

        while not valid:
            response = input(question)
            try:
                response = float(response)
                print("Please enter a word.")
                print()

            except ValueError:
                valid = True
        return response

name = False
while not name:

        # asks for users name
        user = strcheck("What is your name?: ")
        if user == "":
            print("Please enter a word.")
            print()

        else:
            calcu = False
            name = True

            while not calcu:

                loop = False

                print()
                print("Please note {} that this calculator only works with square, rectangles and circles 's, r, c', and will only answered in cm's not m's".format(user))
                shape = strcheck("What shape are you calculating the area and perimeter for?: ").lower()
                print()

                # square area/perimeter calculation
                if shape == "square" or shape == "s":
                    square = intcheck("How long/wide is your square?: ")
                    square = square ** 2
                    squarep = square * 4
                    perimeter = (math.ceil(squarep*100)/100)
                    area = (math.ceil(square*100)/100)
                    print("The Area of your square is {}cm^2".format(area))
                    print("The Perimeter of your square is {}cm".format(perimeter))

                # rectangle area/perimeter calculation
                elif shape == "rectangle" or shape == "r":
                    length = intcheck("What is the length of your rectangle?: ")
                    width = intcheck("What is the width of your rectangle?: ")
                    rectangle = length * width
                    rectanglep = 2 * length + 2 * width
                    perimeter = (math.ceil(rectanglep*100)/100)
                    area = (math.ceil(rectangle*100)/100)
                    print("The Area of your rectangle is {}cm^2.".format(area))
                    print("The Perimeter of your rectangle is {}cm".format(perimeter))

                # circle radius/circumference calculation
                elif shape == "circle" or shape == "c":
                    radius = intcheck("What is the radius of the circle?: ")
                    circle = 2 * math.pi * radius
                    circlea = math.pi * radius ** 2
                    circle = (math.floor(circle*100)/100)
                    circumference = (math.ceil(circlea*100)/100)
                    print("The Area of your circle is {}cm^2.".format(circle))
                    print("The Circumference is {}cm.".format(circumference))

                 # checks if the input is blank
                else:
                    print("Please input one of the choices (s, r, and c are accepted).")
                    loop = True


                while not loop:
                    # asks if user wants to use the calculator again.
                    calcu = strcheck("Do you wish to use the calculator again? if so press enter or type 'y', otherwise type any letter: ").lower()

                    if calcu == "" or calcu == "y" or calcu == "yes":
                        calcu = False
                        loop = True
                        print()
                        print("Welcome back {}".format(user))

                    else:
                        print()
                        print("Thank's for using this calculator {}".format(user))
                        quit()
