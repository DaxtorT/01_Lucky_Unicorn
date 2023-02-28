import random
import time

# Main Routine goes here
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 10):
    chosen_number = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        balance += 4
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        balance -= 1
    else:
        if chosen_number % 2 == 0:
            chosen = "Horse"
        else:
            chosen = "Zebra"
        balance -= 0.5
        
    # Output Balance
    print("You got a {}. Your Balance is ${:.2f}".format(chosen, balance))
    time.sleep(0.5)

print()
print("Your Final Balance is ${:.2f}".format(balance))