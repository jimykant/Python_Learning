"""
==========================================================
User Defined Functions
==========================================================
Description:
    - Functions are reusable blocks of code.
    - They help avoid code repetition.
    - A function executes only when it is called.
"""

"""
----------------------------------------------------------
1. Creating and Calling a Function
----------------------------------------------------------
Description:
    - Define a function using the def keyword.
    - Call the function using its name.
Syntax:
    - def function_name():
          statements
    - function_name()
"""
print("1. Creating and Calling a Function")
def greeting():
    print("Hello, good morning!")
    print("It's a beautiful day.")
greeting()
print("\n")

"""
----------------------------------------------------------
2. Function with Arguments
----------------------------------------------------------
Description:
    - Arguments allow data to be passed into a function.
Syntax:
    - def function_name(argument):
          statements
    - function_name(value)
"""
print("2. Function with Arguments")
def greeting_someone(name):
    print(f"Hello {name}, good morning!")
    print("It's a beautiful day.")
greeting_someone("Jimi")
greeting_someone("John")
print("\n")

"""
----------------------------------------------------------
3. Odd-Even Check Function
----------------------------------------------------------
Description:
    - Check whether a number is odd or even.
Syntax:
    - if condition:
          statements
      else:
          statements
"""
print("3. Odd-Even Check Function")
def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
odd_even(1)
odd_even(2)
odd_even(3)
odd_even(4)
print("\n")

"""
----------------------------------------------------------
4. Function to Add Two Numbers (Using print)
----------------------------------------------------------
Description:
    - Add two numbers and display the result.
    - The value is displayed but not returned.
Syntax:
    - def function_name(arg1, arg2):
          statements
"""
print("1. Function to Add Two Numbers (Using print)")
def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")  # Display result
add(1, 2)
add(3, -4)
print("\n")

"""
==========================================================
Returning Values from Functions
==========================================================
Description:
    - A function can return values using the return keyword.
    - return sends data back to the function caller.
    - Unlike print(), returned values can be stored and reused.
"""
print("# Returning Values from Functions")
"""
----------------------------------------------------------
1. Returning a Value from a Function
----------------------------------------------------------
Description:
    - Return a value instead of printing it.
    - The returned value can be stored in a variable.
Syntax:
    - return value
Note:
    - return immediately exits the function.
"""
print("1. Returning a Value from a Function")
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is even number."  # Return even message
    else:
        return f"{num} is odd number."   # Return odd message
result = even_odd(5)  # Store returned value
print(result)
print("\n")

"""
----------------------------------------------------------
2. Returning Multiple Values from a Function
----------------------------------------------------------
Description:
    - A function can return multiple values.
    - Returned values can be unpacked into variables.
Syntax:
    - return value1, value2, value3
"""
print("2. Returning Multiple Values from a Function")
def arithmetic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division
number1 = int(input("Enter first number: "))  # ask the number from user
number2 = int(input("Enter second number: "))
result1, result2, result3, result4 = arithmetic(number1, number2)  # Unpacking returned values
print(f"\nAddition of {number1} and {number2} is {result1}")
print(f"Subtraction of {number1} and {number2} is {result2}")
print(f"Multiplication of {number1} and {number2} is {result3}")
print(f"Division of {number1} and {number2} is {round(result4, 2)}")
