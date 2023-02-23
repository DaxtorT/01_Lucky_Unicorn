# Functions go here
def num_checker(question, low, high):
    error_1 = "Please enter a number that's more than 0\n"
    error_2 = "Please enter a number that's less than (or equal to) 10\n"
    error_3 = "Please enter a whole number (without decimal point)\n"

    keep_going = ""
    while keep_going == "":
        try:
            # Ask the question
            response = int(input("How much would you like to play with? "))

            # If the amount is too low / too high give
            if  0 < response <= 10:
                print("You have asked to play with ${}\n".format(response))

            # Output error
            elif response < 1:
                print(error_1)

            elif response > 10:
                print(error_2)
            
        except ValueError:
            print(error_3)


# Main Routine goes here

error_1 = "Please enter a number that's more than 0\n"
error_2 = "Please enter a number that's less than (or equal to) 10\n"
error_3 = "Please enter a whole number (without decimal point)\n"

keep_going = ""
while keep_going == "":
    try:
        # Ask the question
        response = int(input("How much would you like to play with? "))

        # If the amount is too low / too high give
        if  0 < response <= 10:
            print("You have asked to play with ${}\n".format(response))

        # Output error
        elif response < 1:
            print(error_1)

        elif response > 10:
            print(error_2)
        
    except ValueError:
        print(error_3)

