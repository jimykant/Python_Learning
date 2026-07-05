"""
==========================================================
Types of Function Arguments
==========================================================
Description:
    - Arguments are values passed to a function.
    - Python supports positional, default, and keyword arguments.
    - These help make functions flexible and reusable.
"""

"""
----------------------------------------------------------
1. Positional Arguments
----------------------------------------------------------
Description:
    - Arguments are assigned based on their position.
    - The first value goes to the first parameter, the second value goes to the second parameter, and so on.
Syntax:
    - function_name(value1, value2)
"""
print("1. Positional Arguments")
def add(a, b):
    return a + b
result = add(10, 5)  # a = 10, b = 5
print(f"Result : {result}")
print("\n")

"""
----------------------------------------------------------
2. Default Arguments
----------------------------------------------------------
Description:
    - Parameters can have default values.
    - If an argument is not provided, the default value is used.
Syntax:
    - def function_name(arg1, arg2=default_value):
          statements
Note:
    - Non-default arguments should not follow default arguments.
    - Wrong : def function_name(a, b=10, c)
    - Correct : def function_name(a, c, b=10)
"""
print("2. Default Arguments")
def add(a, b=10):
    print(f"a : {a}, b : {b}")
    return a + b
result = add(10, 20)  # a = 10, b = 20
print(f"Result : {result}")
result1 = add(5)  # a = 5, b = 10 (default value)
print(f"Result : {result1}")
print("\n")

"""
----------------------------------------------------------
3. Keyword Arguments
----------------------------------------------------------
Description:
    - Arguments are passed using parameter names.
    - The order of arguments does not matter when using keywords.
Syntax:
    - function_name(arg_name=value)
Note:
    - Keyword arguments improve readability.
"""
print("3. Keyword Arguments")
def add(a, b=10, c=10):
    print(f"a : {a}, b : {b}, c : {c}")
    return a + b + c
result = add(10, 5)  # Positional arguments
print(f"Result : {result}")
result1 = add(10, c=20)  # Keyword argument
print(f"Result : {result1}")
print("\n")

"""
==========================================================
Variable Length Arguments
==========================================================
Description:
    - Sometimes we do not know how many arguments will be passed.
    - Python provides *args and **kwargs to handle such situations.
    - *args stores values in a Tuple.
    - **kwargs stores values in a Dictionary.
"""
print("## Variable Length Arguments")
"""
----------------------------------------------------------
1. Variable Length Positional Arguments (*args)
----------------------------------------------------------
Description:
    - *args allows a function to accept 0 to N positional arguments.
    - All arguments are stored as a Tuple.
Syntax:
    - def function_name(*args):
          statements
Note:
    - Wrong : function_name(*args, a)
    - Right : function_name(a, *args)
"""
print("1. Variable Length Positional Arguments (*args)")
def add(*args):
    print(f"Arguments : {args}")  # Tuple containing all positional arguments
    print(f"Type : {type(args)}")
    return sum(args)  # Sum all values in the tuple
result = add(1, 2, 3, 4, 5, 6, 7, 8)
print(f"Sum : {result}")
print("\n")

"""
----------------------------------------------------------
2. Variable Length Keyword Arguments (**kwargs)
----------------------------------------------------------
Description:
    - **kwargs allows a function to accept 0 to N keyword arguments.
    - All keyword arguments are stored as a Dictionary.
Syntax:
    - def function_name(**kwargs):
          statements
Note:
    - Wrong : function_name(**kwargs, a, b); also function_name(**kwargs, *args)
    - Right : function_name(a, b, **kwargs); also function_name(*args, **kwargs) 
"""
print("2. Variable Length Keyword Arguments (**kwargs)")
def student_details(sid, sname, **marks):
    percent = sum(marks.values()) / len(marks)  # Calculate percentage using dictionary values
    print(f"Student ID : {sid}")
    print(f"Student Name : {sname}")
    print(f"Subjects and Marks : {marks}")  # Dictionary of subjects and marks
    print(f"Percentage : {round(percent, 2)}%\n")
student_details(1, "Jimy", eng=78.5, maths=81.0, sci=90.5)
student_details(2, "Komal", eng=70.0, sci=92.5)
