"""
==========================================================
Mutability & Immutability in Python
==========================================================
Description:
    - Mutability means an object can be modified after it is created.
    - Immutability means an object cannot be modified after it is created.
    - Mutable Objects : List, Dictionary, Set
    - Immutable Objects : String, Tuple, Integer, Float
"""

"""
----------------------------------------------------------
1. Strings are Immutable
----------------------------------------------------------
Description:
    - Strings cannot be modified after they are created.
    - Methods like replace() create a new string instead of changing the original.
Syntax:
    - string.replace(old_value, new_value)
"""
print("1. Strings are Immutable")
s1 = "Python is fun"
print(f"Original String : {s1}")
s2 = s1.replace("Python", "Java")
print(f"Original String after replace() : {s1}")
print(f"New String : {s2}")
print("\n")

"""
----------------------------------------------------------
2. Lists are Mutable
----------------------------------------------------------
Description:
    - Lists can be modified after they are created.
    - append() adds a new element to the original list.
Syntax:
    - list.append(element)
"""
print("2. Lists are Mutable")
l1 = [10, 20, 30]
print(f"Original List : {l1}")
l1.append(40)
print(f"List after append() : {l1}")
print("\n")

"""
----------------------------------------------------------
3. Modifying List Elements
----------------------------------------------------------
Description:
    - Individual list elements can be changed using indexing.
    - Lists are mutable, so the original list is updated.
Syntax:
    - list_name[index] = new_value
"""
print("3. Modifying List Elements")
fruits = ["Mango", "Orange", "Aple"]
print(f"Original List : {fruits}")
print(f"Data Type : {type(fruits)}")
print(f"Misspelled Fruit : {fruits[-1]}")
fruits[-1] = "Apple"
print(f"Updated List : {fruits}")
