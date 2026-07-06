"""
==========================================================
Random Module in Python
==========================================================
Description:
    - The random module is used to generate random numbers and perform random operations.
    - It provides functions for random floats, integers, selections, and shuffling.
"""

import random

"""
----------------------------------------------------------
1. random()
----------------------------------------------------------
Description:
    - Returns a random floating-point number.
    - The value is between 0.0 (included) and 1.0 (excluded).
Syntax:
    - random.random()
"""
print("1. random()")
print(random.random())
print(random.random())
print("\n")

"""
----------------------------------------------------------
2. randint()
----------------------------------------------------------
Description:
    - Returns a random integer between the specified range.
    - Both the starting and ending values are included.
Syntax:
    - random.randint(start, end)
"""
print("2. randint()")
print(random.randint(10, 15))
print(random.randint(10, 15))
print("\n")

"""
----------------------------------------------------------
3. choice()
----------------------------------------------------------
Description:
    - Returns a random element from a sequence.
    - The sequence can be a list, tuple, or string.
Syntax:
    - random.choice(sequence)
"""
print("3. choice()")
numbers = [10, 4, 1, 8, 4, 3]
print(f"Number List : {numbers}")
print(f"Random Number : {random.choice(numbers)}")
print(f"Random Number : {random.choice(numbers)}")
print("\n")

"""
----------------------------------------------------------
4. shuffle()
----------------------------------------------------------
Description:
    - Randomly rearranges the elements of a mutable sequence.
    - The original sequence is modified.
Syntax:
    - random.shuffle(sequence)
"""
print("4. shuffle()")
fruits = ["Apple", "Mango", "Cherry"]
print(f"Original Fruits List : {fruits}")
random.shuffle(fruits)
print(f"Shuffled Fruits List : {fruits}")
