# Constants
import random

num_error_1 = "Please enter a number that's more than 0\n"
num_error_2 = "Please enter a number that's less than (or equal to) 10\n"
num_error_3 = "Please enter a whole number (without decimal point)\n"
rounds_played = 0

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
    instructions_statement = statement_deco("-", 3, "*", "How to Play", 3)
    print(instructions_statement)
    print("Playing Lucky Unicorn is very easy.")
    print("All you need to do is pick an amount of money to play with,")
    print("from 1 to 10 dollars not including cents.")
    print("Then you press <enter> to start the game and when playing the next round.")
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

def statement_deco(deco_sides, sides_no, deco_top_bottom, start_statement, three_line):
    # Sets up decoration for sides of statement and top / bottom
    sides = deco_sides * sides_no
    single_statement = f"{sides} {start_statement} {sides}"

    top_bottom = deco_top_bottom * len(single_statement)
    big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

    # Outputs either single or triple line statement
    if three_line == 1:
        return single_statement

    elif three_line ==3:
        return big_statement

# Main Routine goes here
intro_statement = statement_deco("-", 3, "*", "Welcome to The Lucky Unicorn Game", 3)
print(intro_statement)
print()

# Ask user if they have played before
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    print()
    instructions()

else:
    print()

# Ask user how much they want to play with
playing_statement = statement_deco("-", 3, "*", "Let's Get Started", 3)
print(playing_statement)
how_much = num_checker("How much do you want to play with? ", 0, 10)
balance = how_much
print()

# Loop for number of rounds to be played
start_statement = statement_deco("=", 3, "", "Press <Enter> to Start the Game", 1)
play_again = input(start_statement)
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    rounds_statement = statement_deco("", 3, "=", "Round #{}".format(rounds_played), 3)
    print(rounds_statement)

    chosen_number = random.randint(1, 100)

    # Adjust balance
    # If random number between 1 and 5 they get a Unicorn and win $4
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        token_deco = "!"
        token_deco_2 = "!"
        balance += 4

    # If random number between 6 and 36 they get a Donkey and lose $1
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        token_deco = "D"
        token_deco_2 = "D"
        balance -= 1

    # If random number is anything else they get either a Horse or Zebra and lose $0.50    
    else:
        # If number is even then they get a Horse
        if chosen_number % 2 == 0:
            chosen = "Horse"
            token_deco = "H"
            token_deco_2 = "H"
        # If number is odd then they get a Zebra
        else:
            chosen = "Zebra"
            token_deco = "Z"
            token_deco_2 = "Z"
        balance -= 0.5

    # Output Balance
    output_statement = statement_deco(token_deco, 1, token_deco_2, "You got a {}. Your Balance is now ${:.2f}".format(chosen, balance), 3)
    print(output_statement)
    print()

    # End game (auto if out of money, else manual)
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money :(")
        print()

    else:
        play_again = input("Press <Enter> to Play Again or 'xxx' to Quit")


final_statement = statement_deco("-", 3, "*", "Final Results", 3)
print(final_statement)
print()
print("Total Rounds: {}".format(rounds_played))
print("Final Balance: ${:.2f}".format(balance))
print()

