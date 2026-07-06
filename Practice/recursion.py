"""
==========================================================
Recursion
==========================================================
Description:
    - Recursion is a process in which a function calls itself.
    - Recursive calls continue until a stopping condition is reached.
    - Factorial is a common example used to understand recursion.
"""

"""
----------------------------------------------------------
1. Factorial Without Recursion using While Loop
----------------------------------------------------------
Description:
    - Calculate the factorial of a number using a while loop.
    - Factorial of n (n!) = n × (n-1) × (n-2) × ... × 2 × 1
    - Example: 4! = 4 × 3 × 2 × 1 = 24
Syntax:
    - while condition:
          statements
"""
print("1. Factorial Without Recursion using While Loop")
def fact(num):
    factorial = 1  # store the factorial values & it's multiplication so we need to take 1 instead of 0
    while num > 1:  # loop run till (num > 1)
        factorial *= num  # Multiply current number with factorial
        num -= 1  # Move to previous number
    return factorial
number = 5
result = fact(number)
print(f"Factorial of {number} is {result}")
print("\n")

"""
----------------------------------------------------------
2. Factorial Using Recursion
----------------------------------------------------------
Description:
    - Calculate the factorial of a number using recursion.
    - The function calls itself until the base condition is reached.
Syntax:
    - def function_name(num):
          if base_condition:
              return value
          return num * function_name(num - 1)
Note:
    - The base condition prevents infinite recursive calls.
"""
print("2. Factorial Using Recursion")
def fact_rec(num):
    if num == 1:
        return 1  # Base condition
    else:
        factorial = num * fact_rec(num - 1)  # Recursive call
        return factorial
print(f"Factorial of {number} is {fact_rec(number)}")
