keep_going = ""
while keep_going == "":

    error = ("Please answer yes or no.")

    # Ask user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("program continues")
    elif show_instructions == "y":
        print("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no":
        print("display instructions")
    elif show_instructions == "n":
        print("display instructions")

    # If they say anything else, output error
    else:
        print(error)