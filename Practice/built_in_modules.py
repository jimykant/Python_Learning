"""
==========================================================
Python Built-in Modules
==========================================================
Description:
    - A .py file is called a module in Python.
    - Modules contain reusable functions, classes, and variables.
    - Python provides many built-in modules such as:
        - math
        - random
        - datetime
    - Modules help avoid writing the same code repeatedly.
"""
print("Python built-in Modules and it's Usage")
"""
----------------------------------------------------------
1. Importing the Entire Module
----------------------------------------------------------
Description:
    - Import the complete module using the 'import' keyword.
    - Access module-functions using the dot (.) operator.
Syntax:
    - import module_name
    - module_name.function_name()
"""
print("1. Importing the Entire Module")
import math
num = 100
output = math.sqrt(num)  # Calculate square root
print(f"Square Root of {num} is {output}")
# Calculate the area of circle
radius = 5
area_of_circle = math.pi * (radius ** 2)  # Area = πr²
print(f"Area of Circle with Radius {radius} is {round(area_of_circle, 2)}")
print("\n")

"""
----------------------------------------------------------
2. Importing Specific Functions from a Module
----------------------------------------------------------
Description:
    - Import only the required functions from a module.
    - No need to use the module_name while calling the function.
Syntax:
    - from module_name import function_name
    - from module_name import f1, f2, f3
"""
print("2. Importing Specific Functions from a Module")
from random import randint
value = randint(1, 6)  # Generate random integer from 1 to 6
print(f"Dice Value : {value}")
print("\n")

"""
----------------------------------------------------------
3. Importing a Module with an Alias
----------------------------------------------------------
Description:
    - An 'alias' is a short name given to a 'module'.
    - Useful when module names are long.
Syntax:
    - import module_name as alias_name
"""
print("3. Importing a Module with an Alias")
import datetime as dt
t = dt.time(8, 43, 51)  # Create a time object
print(f"Time : {t}")
print("\n")

"""
----------------------------------------------------------
4. Why Use Modules?
----------------------------------------------------------
Description:
    - Modules provide ready-made functionality.
    - They save development time and effort.
Examples:
    - math      -> Mathematical operations
    - random    -> Random values
    - datetime  -> Date and time handling
"""
print("4. Why Use Modules?")
print("math      -> Mathematical Operations")
print("random    -> Random Value Generation")
print("datetime  -> Date and Time Handling")
