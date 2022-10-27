# Area and Perimeter calculator
# Date: 10/9/18
# Author: Aaron Heald
# Version 1: Basic setup with printing of decimals
# Version 2: Allow shorter inputs such as "a" "p"
# Version 3: Allows the use of decimal numbers to be inputted


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
                    print("Please use a positive number!")
                else:
                    print()
                    valid = True
            except ValueError:
                print("Please enter an integer")
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
            print()
            calcu = False
            name = True

            while not calcu:

                pchoice = False
                while not pchoice:
                    calcu = False

                    # asks user what they are calculating
                    choice = strcheck("Are you calculating the Area or Perimeter?: ").lower()

                    # area calculation
                    if choice == "area" or choice == "a":
                        print()
                        shape = strcheck("What shape are you calculating the area for?: ").lower()

                        # square area calculation
                        if shape == "square" or shape == "s":
                            square = intcheck("How long/wide is your square?: ")
                            square = square ** 2
                            area = (math.ceil(square*100)/100)
                            print("The perimeter of your square is {}".format(area))

                        # rectangle area calculation
                        elif shape == "rectangle" or shape == "r":
                            length = intcheck("What is the length of your rectangle?: ")
                            width = intcheck("What is the width of your rectangle?: ")
                            area = length * width
                            rectangle = (math.ceil(area*100)/100)

                        # circle radius calculation
                        elif shape == "circle" or shape == "c":
                            radius = intcheck("What is the radius of the circle?: ")
                            radius = 2 * math.pi * radius
                            circle = (math.floor(radius*100)/100)
                            print(circle)

                    # perimeter calculation
                    elif choice == "perimeter" or choice == "p":
                        print()
                        shape = strcheck("What shape are you calculating the perimeter for?: ").lower()

                        # square perimeter calculation
                        if shape == "square" or shape == "s":
                            square = intcheck("How long/wide is your square?: ")
                            square = square * 4
                            perimeter = (math.ceil(square*100)/100)
                            print("The perimeter of your square is {}".format(perimeter))

                        # rectangle perimeter calculation
                        elif shape == "rectangle" or shape == "r":
                            length = intcheck("What is the length of your rectangle?: ")
                            width = intcheck("What is the width of your rectangle?: ")
                            perimeter = 2 * length + 2 * width
                            rectangle = (math.ceil(perimeter*100)/100)


                        # circle circumference calculation
                        elif shape == "circle" or shape == "c":
                            radius = intcheck("What is the radius of the circle?: ")
                            radius = 2 * math.pi * radius
                            circumference = (math.ceil(radius*100)/100)
                            print(circumference)


                    # checks if the input is blank
                    else:
                        print()
                        print("Please input one of the choices.")
                        calcu = True


                    # asks if user wants to use the calculator again.
                    calcu = strcheck("Do you wish to use the calculator again? if so press enter, otherwise type any letter: ")

                    if calcu == "":
                        calcu = False
                        print()
                        print("Welcome back {}".format(user))

                    else:
                        print()
                        print("Thank's for using this calculator {}".format(user))
                        quit()


