"""
# Mutability & Immutability
1. Mutability
# Objects can be changed after they are created.
# Examples: List, Dictionary, Set

2. Immutability
# Objects cannot be changed after they are created.
# Examples: String, Tuple, Integer, Float
"""

# Strings are Immutable
# Syntax - string.replace(old_value, new_value)
print("1. Strings are Immutable - string.replace(old_value, new_value)")
s1 = "Python is fun"
print(f"Original String : {s1}")
# replace() does not change the original string.
# It creates and returns a new string.
s2 = s1.replace("Python", "Java")
print(f"Original String after replace() : {s1}")
print(f"New String : {s2}")
print("\n")

# Lists are Mutable
# Syntax - list.append(element)
print("2. Lists are Mutable - list.append(element)")
l1 = [10, 20, 30]
print(f"Original List : {l1}")
# append() changes the original list.
l1.append(40)
print(f"List after append() : {l1}")
print("\n")

fruits = ["Mango", "Orange", "Aple"]
print(f"Original List : {fruits} is {type(fruits)}")
print(f"Get the misspelled fruit: {fruits[-1]}")
# change the spelling of this fruit
fruits[-1] = "Apple" # Re-assigning the value
print(f"Re-assigning the value of 'Aple': {fruits}")
