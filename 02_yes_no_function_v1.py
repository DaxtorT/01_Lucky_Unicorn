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

# Main Routine goes here
show_instructions = yes_no("Have you played this game before? ")
print("You choose {}".format(show_instructions))
print()