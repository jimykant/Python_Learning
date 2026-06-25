# Removing Spaces from a String - strip()
print("#Let's see some Functions")
print("1. Removing Spaces from the String")
print("# strip()")
s1 = "   Python  "
print(s1)
s2 = s1.strip()
print(s2)
print(s1 == s2)
print(s2 == s1.strip())
print("\n")

# Replace Function - replace()
print("2. Replace Function")
print("# replace()")
s1 = "We are learning Python"
print(s1)
print(s1.replace("Python", "Java"))
print(s1)
print(s1.replace("l", "L"))
print(s1.replace("e", "E"))
print(s1.replace("e", "E", 1))
print("\n")

# Count Function - Counting Substring from a String
# string.count(substring)
print("3. Count Function")
print("# count()")
s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(f'Occurrences of "{s2}" in "{s1}" is {s1.count(s2)}')
s3 = "e"
print(f'Occurrences of "{s3}" in "{s1}" is {s1.count(s3)}')
s4 = "ing"
print(f'Occurrences of "{s4}" in "{s1}" is {s1.count(s4)}')
print("\n")

# Changing Case of a String
# upper(), lower(), title(), capitalize()
print("4. Changing Case Function")
s1 = "We are Learning Python. python is Fun"
print(s1)

# upper()
print("# upper()")
print(s1.upper())
# lower()
print("# lower()")
print(s1.lower())
# title()
print("# title()")
print(s1.title())
# capitalize
print("# capitalize()")
print(s1.capitalize())
print("\n")

# Startswith and Endswith of a String
# startswith(), endswith()
print("5. Startswith and Endswith Functions")
s1 = "We are Learning Python."
print(s1)

# startswith()
# string.startswith(substring)
print("# startswith()")
print(s1.startswith("We"))
print(s1.startswith("we"))

# endswith()
# string.endswith(substring)
print("# endswith()")
print(s1.endswith("python"))
print(s1.endswith("Python"))
print(s1.endswith("Python."))
