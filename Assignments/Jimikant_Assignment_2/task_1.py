"""
Assignment 2'
Task 1 :- Check if a Number is Even or Odd
"""

number = int(input("Enter a Number: "))
if number % 2 == 0:
    odd_even = "even"
else:
    odd_even = "odd"
print(f"{number} is an {odd_even} number")
