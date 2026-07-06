# ==========================================================
# File Name : user_define_modules_main.py
# ==========================================================
"""
==========================================================
User Defined Modules
==========================================================
Description:
    - A user-defined module is a Python file created by the programmer.
    - Functions, variables, and classes can be stored inside it.
    - Other Python files can import and use them.
    - Here we import:
        user_define_modules_sub.py
"""
print("# User Defined Module (Main Module)")

# Provide an alias to make function calls shorter.
import user_define_modules_sub as arithmetic

"""
----------------------------------------------------------
1. Using the Addition Function
----------------------------------------------------------
Description:
    - Call the add() function from the imported module.
Syntax:
    - alias_name.function_name(arguments)
"""
print("1. Using the Addition Function")

a = 100
b = 20

result = arithmetic.add(a, b)  # Call add() from the imported module
print(f"Addition of {a} and {b} is {result}")
print("\n")

"""
----------------------------------------------------------
2. Using the Square Root Function
----------------------------------------------------------
Description:
    - Call the square_root() function from the imported module.
"""
print("2. Using the Square Root Function")

result = arithmetic.square_root(a)  # Call square_root() from the imported module
print(f"Square Root of {a} is {result}")
