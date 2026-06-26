"""
==========================================================
Sets in Python
==========================================================
Description:
    - Sets are unordered (non-sequential) collections of unique elements.
    - Duplicate values are automatically removed.
    - Elements are enclosed within curly braces {}.
"""

"""
----------------------------------------------------------
1. Creating a Set
----------------------------------------------------------
Description:
    - Creates a set containing different types of elements.
Syntax:
    - set_name = {element1, element2, element3, ...}
Note:
    - A set can store elements of different data types.
"""
print("1. Creating a Set")
set1 = {10, "Python", 2.5}
print(f"Set is: {set1}")
print(f"Type of set1 is: {type(set1)}")
print("\n")

"""
----------------------------------------------------------
2. Indexing in Set
----------------------------------------------------------
Description:
    - Sets do NOT support indexing because they are unordered collections.
Syntax:
    - set[index]
Note:
    - Attempting to access an element using an index raises TypeError: 'set' object is not subscriptable.
"""
print("2. Indexing in Set")
# print(set1[0])      # ❌ TypeError: 'set' object is not subscriptable
print("\n")

"""
----------------------------------------------------------
3. Length of the Set
----------------------------------------------------------
Description:
    - Returns the total number of unique elements present in the set.
Syntax:
    - len(set)
Note:
    - Duplicate elements are counted only once.
"""
print("3. Length of the Set - len(set)")
set1 = {10, "Python", 2.5, 50, 100}
print(f"Set is: {set1}")
print(f"Length of the set is: {len(set1)}")
print("\n")

"""
----------------------------------------------------------
4. Duplicate Elements in Set
----------------------------------------------------------
Description:
    - Sets store only unique elements. Duplicate values are automatically removed.
Syntax:
    - set_name = {value1, value2, value3, ...}
Note:
    - Even if duplicate values are provided, only one copy of each value is stored in the set.
"""
print("4. Duplicate Elements in Set")
set2 = {10, 20, 30, 10, 40, 20, 50, 30, 10}
print("Original values entered : 10, 20, 30, 10, 40, 20, 50, 30, 10")
print(f"Set after removing duplicate elements : {set2}")
print(f"Length of the set is: {len(set2)}")
