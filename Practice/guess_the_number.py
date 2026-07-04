"""
==========================================================
Number Guessing Game
==========================================================
Description:
    - Generate a random number and let the user guess it.
    - The user gets 10 attempts to guess the correct number.
    - The game ends immediately if the user guesses correctly.
    - Provide some hints to the user for guessing the number.
"""

import random

"""
----------------------------------------------------------
1. Number Guessing Game
----------------------------------------------------------
Description:
    - Generate a secret number between 1 and 50.
    - Give the user 10 chances to guess it.
    - Provide hints whether the secret number is higher or lower.
Syntax:
    - random.randint(start, end)
    - while condition:
          statements
Note:
    - break exits the loop immediately.
    - A boolean flag is used to track whether the guess is correct.
"""
print("1. Number Guessing Game")
print("Welcome to the Number Guessing Game. You have 10 attempts to guess the number")
print("The secret number is between 1 and 50")
attempt_no = 1
secret_number = random.randint(1, 50)
# print(secret_number)
attempts_left = 10
is_guess_correct = False
while attempt_no <= 10:
    print(f"\nYou have {attempts_left} attempts left")
    user_number = int(input("Guess the number: "))
    if user_number == secret_number:
        print(f"Congrats! You guessed the number in {attempt_no} attempts")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_lower = "higher"
        else:
            higher_lower = "lower"
        print(f"Your guess is wrong! Try {higher_lower} number")
    attempt_no += 1
    attempts_left -= 1
if not is_guess_correct:
    print("Bad luck! You exhausted all your attempts and couldn't guess the number.")
print(f"The secret number was {secret_number}")
print("Game Over!!!")
