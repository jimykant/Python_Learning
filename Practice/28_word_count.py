"""
==========================================================
Searching and Counting Elements Using for Loop
==========================================================
Description:
    - A for loop can be used to search elements in a sequence.
    - A counter variable can be used to count matching elements.
    - Matching elements can be stored in a list for later use.
"""

"""
----------------------------------------------------------
1. Count Countries Starting with 'I'
----------------------------------------------------------
Description:
    - Checks the first character of each country name.
    - Counts all countries starting with 'I'.
    - Stores matching countries in a separate list.
Syntax:
    - if string[index] == value:
          statement
"""
print("1. Count Countries Starting with 'I'")

countries = ["India", "United States", "Australia", "Ireland",
             "Shri Lanka", "Iceland", "Cuba", "Iran", "Iraq", "Poland"]
counter = 0
output = []
for country in countries:
    # Check whether the first character is 'I'
    if country[0] == "I":
        # Increase the count
        counter += 1
        # Store matching country
        output.append(country)
print(f"Count : {counter}")
print(f"Countries : {output}")
print("\n")

"""
----------------------------------------------------------
2. Count Countries Using startswith()
----------------------------------------------------------
Description:
    - startswith() checks whether a string begins with a specified value.
    - It is more readable and safer than checking indexes directly.
    - Counts all countries starting with 'I'.
Syntax:
    - string.startswith(value)
"""
print("2. Count Countries Using startswith()")
counter = 0
output = []
for country in countries:
    # Check whether the country starts with 'I'
    if country.startswith("I"):
        # Increase the count
        counter += 1
        # Store matching country
        output.append(country)
print(f"Count : {counter}")
print(f"Countries : {output}")
