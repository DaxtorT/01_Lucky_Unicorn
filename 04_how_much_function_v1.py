# Constants
error_1 = "Please enter a number that's more than 0\n"
error_2 = "Please enter a number that's less than (or equal to) 10\n"
error_3 = "Please enter a whole number (without decimal point)\n"

# Functions go here
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
                print(error_1)

            elif response > max_value:
                print(error_2)
        
        except ValueError:
            print(error_3)


# Main Routine goes here
how_much = num_checker("How much do you want to play with? ", 0, 10)

print("You have asked to play with ${}".format(how_much))
print()