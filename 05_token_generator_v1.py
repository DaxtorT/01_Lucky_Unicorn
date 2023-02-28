import random

# Main Routine goes here

tokens = ["unicorn", "zebra", "donkey", "horse"]

# Testing loop to generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')