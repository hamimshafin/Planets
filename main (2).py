"""
Usage: main.py
A calculator that shows the distance between two planets chosen by the user
Coded primarily using Code With Me, hosted by either Hudson or Mason

GitHub: https://github.com/HuddyP/PlanetsCalc

"""


# metadata
__authors__ = "Hudson Pfenning, Hamim Shafin, Mason Regier"
__creation_date__ = "2/1/24"
__emails__ = "hupfen01@wsc.edu, maregi01@wsc.edu, hashaf01@wsc.edu "
__version__ = "0.0.1"

#formatting the single and the double dash lines
dash_length = 40
single_divider = ('-' * dash_length)
double_divider = ('=' * dash_length)

#tuple list for all the planets
planets = (
    ("Mercury", 57),
    ("Venus", 108),
    ("Earth", 150),
    ("Mars", 228),
    ("Jupiter", 779),
    ("Saturn", 1430),
    ("Uranus", 2880),
    ("Neptune", 4500),
)

def display_planets_menu():
    """
    displays the planets as a menu in main
    Made by Hamim
    :return: planet name and distance tuple as list
    """
    print(double_divider)
    print('Planet\'s Average Distance From Sun')
    print(double_divider)

    menu_num = 1

    for planet_name, planet_dist in planets:
        print(f"{menu_num}: {planet_name:<7} = {planet_dist:>4} million miles")
        menu_num += 1

    print(single_divider)

def get_integer_output(message, min_num=0, max_num=8):
    """
    Processes the planet inputs made by user and ties that input to a value in main
    If inputted value isn't within the range or a valid input then input request repeats until valid input is made
    Made by Everyone
    :param message: prompt for user to input a number
    :param min_num: lowest possible number for user to input without receiving error
    :param max_num: highest possible number for user to input without receiving error
    :return: user input
    """
    while True: #keep looping until the user enters a valid value
        #prevent the program from ending due to a ValueError runtime error
        try:
            user_input = int(input(message))

            if min == 0 and max == 8:
                return user_input
            elif min_num <= user_input <= max_num:
                return user_input
            else:
                print(f"\tInvalid input: Please enter a number between {min_num} and {max_num}.")
                continue
        except ValueError:
            print(f"\tInvalid input: Please enter a number.")
            continue

def display_abs_distance(planet1_num,planet2_num):
    """
     Takes both inputted planet values and determines their location in the tuple
     Ties values found to either planet1 or planet2 name, dist and info
     Calculates difference in distance between planets and outputs the resulting difference
     Made by Hudson and Mason
     :param planet1_num: planet value inputted by user as first planet
     :param planet2_num: planet value inputted by user as second planet
     :return: calculated total distance between selected planets
    """

    #grabs planet info based on user input and binds information to planet1_name, dist and info
    planet1_info = planets[planet1_num - 1]
    planet1_name, planet1_dist = planet1_info

    # grabs planet info based on user input and binds information to planet2_name, dist and info
    planet2_info = planets[planet2_num - 1]
    planet2_name, planet2_dist = planet2_info

    #determines which planet distance is larger and calculates based on results of if-elif statement
    if planet2_dist > planet1_dist:
        calculate_dist = planet2_dist - planet1_dist
    elif planet1_dist > planet2_dist:
        calculate_dist = planet1_dist - planet2_dist

    print("The distance between " + planet1_name + " and " + planet2_name + " is " + str(calculate_dist) + " miles")

def main():
    """
     Welcomes user to calculator, then asks user to input two numbers for planets. If user enters 0 then program ends
     After receiving inputs, determines if either inputted value is 0, if not, runs two instances of get_integer_output
     Once both get_integer_output functions are ran, program runs display_abs_distance using resulting values from get_integer_output
     Prompts user to press any key to continue, and program loops
     Made by Everyone
     :param planet1_num: user's selection as first planet
     :param planet2_num: user's selection as second planet
     :param end_input: user presses any key to restart program
     :return: welcomes user, introduces calculator inputs, gives resulting calculation, asks user to press any key to restart, and says goodbye if 0 is pressed
    """
    print(double_divider)
    print("Welcome to the Planet Calculator")
    print(double_divider)

    display_planets_menu()
    print("To calculate the distance between two planets")

    #initial while loop for "beginning" of calculator
    while True:
        print("Enter two planet numbers or type 0 to exit program: ")
        print(single_divider)

        #gets user input for planet1 and runs that instance of get_integer_output.
        planet1_num = get_integer_output("Please enter the first planet: ", min_num=0, max_num=len(planets))
        #program breaks if user inputs 0
        if planet1_num == 0:
            print(double_divider)
            print("Live Long and Prosper")
            print(double_divider)
            break

        while True:
            # gets user input for planet2 and runs that instance of get_integer_output.
            planet2_num = get_integer_output("Please enter the second planet: ", min_num=0, max_num=len(planets))

            # inner while loop breaks if user inputs 0
            if planet2_num == 0:
                print(double_divider)
                print("Live Long and Prosper")
                print(double_divider)
                break
            #if user inputted any value but zero, inner while loop still breaks, but with an actual value to tie to planet2
            else:
                break

        #prints error and breaks if planet1 and planet2 inputted values are the same
        if planet1_num == planet2_num:
            print("Both planets given are the same, please try again")
            break
        #if either planet input is 0, then entire program breaks
        elif planet1_num == 0 or planet2_num == 0:
            break

        display_abs_distance(planet1_num, planet2_num)

        #continues the program with any user input
        input("Press any key to continue: ")

if __name__ == '__main__':
    main()
