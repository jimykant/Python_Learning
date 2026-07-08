"""
Assignment 3
Task 2 :- Using the Math Module for Calculations

Description:-

* Asks the user for a number as input.
* Uses the math module to calculate the:-
  * Square root of the number
  * Natural logarithm (log base e) of the number
  * Sine of the number (in radians)
"""

import math
from task_1 import validation

number = validation()
print()

# Square Root of a Number
square_root = math.sqrt(number)
print(f"Square Root: {round(square_root, 4)}")
print()

# Natural Logarithm (log base e)
logarithm = math.log(number)
print(f"Logarithm : {round(logarithm, 4)}")
print()

# Sine of a Number (Radians)
sine_value = math.sin(number)
print(f"Sine: {round(sine_value, 4)}")
