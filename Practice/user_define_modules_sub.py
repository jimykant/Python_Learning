# ==========================================================
# File Name : user_define_modules_sub.py
# ==========================================================
"""
==========================================================
User Defined Module (Sub Module)
==========================================================
Description:
    - This file acts as a user-defined module.
    - It contains reusable functions.
    - These functions can be imported and used in other Python files.
    - Module Name:
        user_define_modules_sub.py
"""
"""
----------------------------------------------------------
1. Addition Function
----------------------------------------------------------
Description:
    - Adds two numbers and returns the result.
Syntax:
    - add(num1, num2)
"""
def add(num1, num2):
    return num1 + num2

"""
----------------------------------------------------------
2. Square Root Function
----------------------------------------------------------
Description:
    - Calculates the square root of a number.
Syntax:
    - square_root(number)
"""
def square_root(num):
    return num ** 0.5

print("\n")

"""
----------------------------------------------------------
3. __name__ Variable (Dunder Variable)
----------------------------------------------------------
Description:
    - __name__ is a special built-in variable in Python.
    - It helps identify how a Python file is being executed.

Possible Values:
    1. "__main__"
       - When this file is executed directly.

    2. "user_define_modules_sub"
       - When this file is imported into another Python file.

Purpose:
    - Prevent test/demo code of the module from running automatically when the module is imported.
Syntax:
    - if __name__ == "__main__":
          # Executable code
"""

# Display the current value of __name__
print(f"'__name__' (Dunder Variable) Value => {__name__}\n")

# Execute the below code only when this file is run directly
if __name__ == "__main__":
    print("3. Testing Functions Inside the Module")
    a = 200
    result = square_root(a)  # Call square_root() function
    print(f"Square Root of {a} is {round(result, 2)}")
