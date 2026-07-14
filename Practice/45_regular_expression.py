"""
==========================================================
REGULAR EXPRESSIONS (RegEx) IN PYTHON
==========================================================
Description:
    - Regular Expressions (RegEx) are patterns used to search,
      match, validate, extract, and manipulate text.
    - Python provides the built-in 're' module for working
      with Regular Expressions.
Why Use RegEx?
    - Search for specific text patterns.
    - Validate emails, phone numbers, passwords, etc.
    - Extract useful information from large text.
    - Replace or split text based on patterns.
Common Functions:
    - re.search()  -> Find first match.
    - re.findall() -> Find all matches.
    - re.match()   -> Match at beginning of string.
    - re.sub()     -> Replace matching text.
"""
import re

message = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10"
"""
----------------------------------------------------------
1. Search Text Using Normal String Methods
----------------------------------------------------------
Description:
    - Searches text without using RegEx.
    - Useful for simple text searches.
    - 'in' operator returns True or False.
    - find() returns the index of the first occurrence.
Syntax:
    - substring in string
    - string.find(substring)
Note:
    - Suitable for simple searches.
    - Cannot perform advanced pattern matching.
"""
print("1. Search Text Using Normal String Methods")
print(f"'Python' Found : {'Python' in message}")
print(f"Index Of '3.13' : {message.find('3.13')}")
print("\n")

"""
----------------------------------------------------------
2. Search Pattern Using re.search()
----------------------------------------------------------
Description:
    - Searches a string for the first occurrence of a pattern.
    - Returns a Match Object if found.
    - Returns None if no match exists.
Syntax:
    - re.search(pattern, string)
Note:
    - Search starts from left to right.
    - Stops after finding the first match.
"""
print("2. Search Pattern Using re.search()")

# Search for the first occurrence of "13"
match_obj = re.search("13", message)
print(f"Match Object : {match_obj}")
print(f"match Value: {message[32:34]}")
print("\n")

r"""
----------------------------------------------------------
3. Common RegEx Special Characters
----------------------------------------------------------
Description:
    - RegEx provides special characters called shortcuts.
    - They make pattern writing easier and shorter.
Common Shortcuts:
    - [0-9] matches any digit.
    - \d -> Any digit [0-9]
    - \D -> Any non-digit character
    - \s -> Any whitespace character
    - \S -> Any non-whitespace character
    - \w -> Any word character [A-Z, a-z, 0-9, _]
    - \W -> Any non-word character
Note:
    - Character classes represent a group or range of characters.
    - Prefixing a string with r creates a Raw String.
    - Raw strings prevent Python from interpreting
      backslashes (\) as escape characters.
"""
print("3. Common RegEx Special Characters")
"""
----------------------------------------------------------
3.1 Character Classes and Dot Operator
----------------------------------------------------------
Description:
    - [.] matches an actual dot character.
    - . matches any single character except newline.
"""
print("3.1 Character Classes and Dot Operator")

# Search version numbers such as 3.13
# [.] => matches actual dot character
print("for [.]")
match_obj = re.search("[0-9][.][0-9][0-9]", message)
print(f"Match Object : {match_obj}")

# Dot (.) is a special RegEx character
# It matches any character except newline (\n)
print("for .")
match_obj = re.search("[0-9].[0-9]", "House number: 251/A")
print(f"Match Object : {match_obj}")
print("\n")

"""
----------------------------------------------------------
3.2 Using [A-Z] and [a-z]
----------------------------------------------------------
Description:
    - [A-Z] matches uppercase letters.
    - [a-z] matches lowercase letters.
"""
print("3.2 Using [A-Z] and [a-z]")

# r creates a raw string
pat = r"[A-Z][a-z][a-z]"
match_obj = re.search(pat, message)
print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")
print("\n")

r"""
----------------------------------------------------------
3.3 Using \d and \D
----------------------------------------------------------
Description:
    - \d matches one digit, Similar to [0-9].
    - \D matches one non-digit character.
"""
print("3.3 Using \\d and \\D")

# \d matches one digit
print("for \\d")
pat = r"[a-z][a-z] \d"
match_obj = re.search(pat, message)
print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")

# \D matches one non-digit character
print("for \\D")
pat = r"[A-Z][a-z][a-z]\D"
match_obj = re.search(pat, message)
print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")
print("\n")

r"""
----------------------------------------------------------
3.4 Using \s and \S
----------------------------------------------------------
Description:
    - \s matches white-space, tab and new-line character.
    - \S matches any character except white-space, tab and new-line character.
"""
print("3.4 Using \\s and \\S")

# \s matches a space character
print("for \\s")
pat = r"[a-z][a-z]\s[a-z][a-z]"
match_obj = re.search(pat, message)

print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")

# \S matches a non-space character
print("for \\S")
pat = r"[a-z][a-z][a-z]\S[a-z]"
match_obj = re.search(pat, message)

print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")
print("\n")

r"""
----------------------------------------------------------
3.5 Using \w and \W
----------------------------------------------------------
Description:
    - \w matches word characters [A-Z], [a-z], [0-9] and _.
    - \W matches any character except word characters.
"""
print("3.5 Using \\w and \\W")

# \w matches letters, digits, and underscore
print("for \\w")
pat = r"[a-z][a-z][a-z]\w[a-z]"
match_obj = re.search(pat, message)

print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")

# \W matches non-word characters
print("for \\W")
pat = r"[a-z][a-z][a-z]\W[a-z]"
match_obj = re.search(pat, message)

print(f"Pattern : {pat}")
print(f"Match Object : {match_obj}")
