import random

balance = 5
rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{}***".format(rounds_played))

    chosen_number = random.randint(1, 100)

    # Adjust balance
    # If random number between 1 and 5 they get a Unicorn and win $4
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        balance += 4

    # If random number between 6 and 36 they get a Donkey and lose $1
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        balance -= 1

    # If random number is anything else they get either a Horse or Zebra and lose $0.50    
    else:
        # If number is even then they get a Horse
        if chosen_number % 2 == 0:
            chosen = "Horse"
        # If number is odd then they get a Zebra
        else:
            chosen = "Zebra"
        balance -= 0.5

    # Output Balance
    print("You got a {}. Your Balance is now ${:.2f}".format(chosen, balance))

    # End game (auto if out of money, else manual)
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money :(")

    else:
         play_again = input("Press enter to play again or 'xxx' to quit")

print()
print("Final Balance: ${}".format(balance))