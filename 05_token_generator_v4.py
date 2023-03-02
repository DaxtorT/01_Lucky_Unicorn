import random
import time

# Main Routine goes here
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 10 tokens
for item in range(0, 10):
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
    print("You got a {}. Your Balance is ${:.2f}".format(chosen, balance))
    time.sleep(0.5)

print()
print("Your Starting Balance is ${:.2f}".format(STARTING_BALANCE))
print("Your Final Balance is ${:.2f}".format(balance))