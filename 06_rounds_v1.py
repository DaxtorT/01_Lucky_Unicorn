balance = 5
rounds_played = 0

play_again = input("Press <Enter> to play...")
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print(rounds_played)
    balance -= 1
    print("Balance: ", balance)
    print()

    play_again = input("Press enter to play again or 'xxx' to quit")

print()
print("Final Balance", balance)