"""
==========================================================
Dice Rolling Simulator
==========================================================

Description:
    - This program simulates rolling a die.
    - A die has 6 faces numbered from 1 to 6.
    - The program generates a random number between 1 and 6.
    - The user can roll the dice multiple times or quit the game.
"""

import random
"""
Description:
    - Press Enter to roll the dice.
    - Enter 'q' to quit the game.
    - random.randint(1, 6) generates a random number between 1 and 6.
Syntax:
    - random.randint(start, end)
"""
print("Dice Rolling Simulator")

print("Welcome to the Game of Rolling a Dice.")

# Infinite loop runs until the user chooses to quit
while True:
    # Get user input
    choice = input("Press 'Enter' to roll a dice or 'q' to quit : ")
    # Remove leading and trailing spaces
    choice = choice.strip()
    # Exit the game if user enters 'q'
    if choice == "q":
        print("Thanks for playing. Bye!")
        break
    # Roll the dice if user presses Enter
    elif choice == "":
        # Generate a random number between 1 and 6
        number = random.randint(1, 6)
        print(f"Your Number : {number}")
    # Handle invalid input
    else:
        print("Please enter a valid input.")

print("GAME OVER!!!")
