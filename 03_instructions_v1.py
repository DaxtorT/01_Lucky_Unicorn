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

# Main Routine goes here
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()
    print("Program Continues")

else:
    print()
    print("Program Continues")