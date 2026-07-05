"""
==========================================================
Doc Strings
==========================================================
Description:
    - Doc strings are used to describe the purpose of a function.
    - They help other programmers understand what a function does.
    - A doc string should be the first statement inside a function.
"""
"""
----------------------------------------------------------
1. Creating a Doc String
----------------------------------------------------------
Description:
    - A doc string provides information about a function.
    - The help() function displays the doc string.
Syntax:
    - def function_name():
          \"\"\"Doc String\"\"\"
          statements
"""
print("1. Creating a Doc String")
def func():
    """
    This is a doc string.
    We can write what the function is supposed to do.
    :return: None
    """
    return None
help(func)
print("\n")

"""
----------------------------------------------------------
2. Doc String with Parameters and Return Value
----------------------------------------------------------
Description:
    - A doc string can describe parameters and return values.
    - Useful for documentation and code readability.
Syntax:
    - :param parameter_name: Description
    - :return: Description
"""
print("2. Doc String with Parameters and Return Value")
def divide(num1, num2):
    """
    :param num1: A number to be divided (Numerator)
    :param num2: A number that divides num1 (Denominator)
    :return: float (if num2 isn't 0) OR str (if num2 is 0)
    """
    if num2 == 0:
        return "Can't divide by 0"
    else:
        result = num1 / num2
        return result
help(divide)
print(f"Result : {divide(10, 0)}")
