"""
==========================================================
String Operations in Python
==========================================================
Description:
    - Strings support various operations such as concatenation, repetition,
      membership testing, and comparison.
    - These operations help manipulate and compare string values.
"""

"""
----------------------------------------------------------
1. String Concatenation
----------------------------------------------------------
Description:
    - Concatenation joins two or more strings into a single string.
Syntax:
    - string1 + string2
"""
print("1. String Concatenation")
language = "Python "
version = "3.13.3"
print(f"Concatenated String : {language + version}")
print("\n")

"""
----------------------------------------------------------
2. String Repetition
----------------------------------------------------------
Description:
    - Repetition duplicates a string a specified number of times.
    - A string can only be multiplied by an integer.
Syntax:
    - string * integer
"""
print("2. String Repetition")
print(f"'Python' * 4 : {'Python' * 4}")
print("\n")

"""
----------------------------------------------------------
3. Membership Operators
----------------------------------------------------------
Description:
    - The 'in' operator checks whether a substring exists in a string.
    - The 'not in' operator checks whether a substring does not exist in a string.
Syntax:
    - substring in string
    - substring not in string
"""
print("3. Membership Operators")
s1 = "Python is fun"
print(f"String : {s1}")
print(f"'Python' in s1 : {'Python' in s1}")
print(f"'i' in s1 : {'i' in s1}")
print(f"'z' in s1 : {'z' in s1}")
print(f"'Java' in s1 : {'Java' in s1}")
print(f"'Python' not in s1 : {'Python' not in s1}")
print(f"'i' not in s1 : {'i' not in s1}")
print(f"'z' not in s1 : {'z' not in s1}")
print(f"'Java' not in s1 : {'Java' not in s1}")
print("\n")

"""
----------------------------------------------------------
4. String Comparison
----------------------------------------------------------
Description:
    - Comparison operators compare two strings.
    - They return either True or False.
Syntax:
    - string1 == string2
    - string1 != string2
"""
print("4. String Comparison")
print(f"'Python' == 'Python' : {'Python' == 'Python'}")
print(f"'Python' != 'Python' : {'Python' != 'Python'}")
