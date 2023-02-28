import random
import time

# Main Routine goes here

tokens = ["unicorn", "zebra", "donkey", "horse"]
balance = 100

# Testing loop to generate 20 tokens
for item in range(0, 100):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "horse" or "zebra":
        balance -= 0.5
    else:
        balance -= 1

    # Output Token and Balance
    print("Token: {} , Balance: ${}".format(chosen, balance))
    time.sleep(1)