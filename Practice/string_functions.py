"""
==========================================================
Common String Functions in Python
==========================================================
Description:
    - String functions are built-in methods used to perform various operations on strings.
    - They help in modifying, searching, counting, and checking string values.
"""

"""
----------------------------------------------------------
1. Removing Spaces from a String
----------------------------------------------------------
Description:
    - strip() removes leading and trailing whitespace from a string.
    - It returns a new string without modifying the original string.
Syntax:
    - string.strip()
"""
print("1. Removing Spaces from a String")
s1 = "   Python  "
print(f"Original String : '{s1}'")
s2 = s1.strip()
print(f"After strip() : '{s2}'")
print(f"s1 == s2 : {s1 == s2}")
print(f"s2 == s1.strip() : {s2 == s1.strip()}")
print("\n")

"""
----------------------------------------------------------
2. Replacing Substrings
----------------------------------------------------------
Description:
    - replace() replaces a specified substring with another substring.
    - It returns a new string without changing the original string.
Syntax:
    - string.replace(old_value, new_value)
    - string.replace(old_value, new_value, count)
"""
print("2. Replacing Substrings")
s1 = "We are learning Python"
print(f"Original String : {s1}")
print(f"Replace 'Python' with 'Java' : {s1.replace('Python', 'Java')}")
print(f"Original String : {s1}")
print(f"Replace 'l' with 'L' : {s1.replace('l', 'L')}")
print(f"Replace 'e' with 'E' : {s1.replace('e', 'E')}")
print(f"Replace first 'e' with 'E' : {s1.replace('e', 'E', 1)}")
print("\n")

"""
----------------------------------------------------------
3. Counting Substrings
----------------------------------------------------------
Description:
    - count() returns the number of occurrences of a substring.
Syntax:
    - string.count(substring)
"""
print("3. Counting Substrings")
s1 = "We are learning Python. Python is fun."
print(f"String : {s1}")
print(f"Occurrences of 'Python' : {s1.count('Python')}")
print(f"Occurrences of 'e' : {s1.count('e')}")
print(f"Occurrences of 'ing' : {s1.count('ing')}")
print("\n")

"""
----------------------------------------------------------
4. Changing the Case of a String
----------------------------------------------------------
Description:
    - String case methods change the letter case of a string.
Syntax:
    - string.upper()
    - string.lower()
    - string.title()
    - string.capitalize()
"""
print("4. Changing the Case of a String")
s1 = "We are Learning Python. python is Fun"
print(f"Original String : {s1}")
print(f"Upper Case : {s1.upper()}")
print(f"Lower Case : {s1.lower()}")
print(f"Title Case : {s1.title()}")
print(f"Capitalize : {s1.capitalize()}")
print("\n")

"""
----------------------------------------------------------
5. Checking Prefix and Suffix
----------------------------------------------------------
Description:
    - startswith() checks whether a string starts with a specified substring.
    - endswith() checks whether a string ends with a specified substring.
Syntax:
    - string.startswith(substring)
    - string.endswith(substring)
"""
print("5. Checking Prefix and Suffix")
s1 = "We are Learning Python."
print(f"String : {s1}")
print(f"Starts with 'We' : {s1.startswith('We')}")
print(f"Starts with 'we' : {s1.startswith('we')}")
print(f"Ends with 'python' : {s1.endswith('python')}")
print(f"Ends with 'Python' : {s1.endswith('Python')}")
print(f"Ends with 'Python.' : {s1.endswith('Python.')}")
