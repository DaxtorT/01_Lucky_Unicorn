show_instructions = ""
while show_instructions.lower() != "xxx":

    error = ("Please answer yes or no.")

    # Ask user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")

    # If they say anything else, output error
    else:
        print(error)