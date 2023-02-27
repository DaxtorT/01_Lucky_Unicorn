# Constants
num_error_1 = "Please enter a number that's more than 0\n"
num_error_2 = "Please enter a number that's less than (or equal to) 10\n"
num_error_3 = "Please enter a whole number (without decimal point)\n"

# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        # If they say anything else, output error
        else:
            print("Please answer yes / no.")
            print()

def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

def num_checker(question, min_value, max_value):
    keep_going = ""
    while keep_going == "":
        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low / too high give
            if  min_value < response <= max_value:
                return response

            # Output error
            elif response < min_value + 1:
                print(num_error_1)

            elif response > max_value:
                print(num_error_2)
        
        except ValueError:
            print(num_error_3)

# Main Routine goes here
# Ask user if they have played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

else:
    print()

# Ask user how much they want to play with
how_much = num_checker("How much do you want to play with? ", 0, 10)

print("You have asked to play with ${}".format(how_much))
print()

