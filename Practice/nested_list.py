"""
==========================================================
Nested Lists in Python
==========================================================
Description:
    - A nested list is a list that contains one or more lists as its elements.
    - It allows us to store data in multiple levels (a list inside another list).
"""

"""
----------------------------------------------------------
1. Creating a Nested List
----------------------------------------------------------
Description:
    - Creates a list containing different data types, including another list.
Syntax:
    - list_name = [element1, element2, ..., [nested_elements]]
"""
print("1. Creating a Nested List")
l1 = [5, 1.5, "Python", True, None, [1, 2, 3], 10]
print(f"List-1 : {l1}")
print(f"Length : {len(l1)}")
print("\n")

"""
----------------------------------------------------------
2. Accessing a Nested List
----------------------------------------------------------
Description:
    - Access a nested list using indexing.
Syntax:
    - list_name[index]
"""
print("2. Accessing a Nested List")
print(f"Nested List : {l1[-2]}")
print(f"Second Last Element : {l1[-2]}")
print("\n")

"""
----------------------------------------------------------
3. Accessing Elements of a Nested List
----------------------------------------------------------
Description:
    - Access elements inside a nested list using multiple indexes.
Syntax:
    - list_name[index][nested_index]
"""
print("3. Accessing Elements of a Nested List")
print(f"First Element : {l1[-2][0]}")
print(f"Last Element : {l1[-2][-1]}")
print("\n")

"""
----------------------------------------------------------
4. Multiple Nested Lists
----------------------------------------------------------
Description:
    - A list can contain multiple nested lists.
Syntax:
    - list_name = [[...], [...], [...]]
"""
print("4. Multiple Nested Lists")
l2 = [[1, 2], [3, 4], [5, 6, [0, 1]]]
print(f"List-2 : {l2}")
print(f"Length : {len(l2)}")
print(f"Last Nested List : {l2[-1]}")
print("\n")

"""
----------------------------------------------------------
5. Accessing Elements from Multiple Nested Lists
----------------------------------------------------------
Description:
    - Access elements from nested lists using multiple indexes.
Syntax:
    - list_name[index][nested_index]
"""
print("5. Accessing Elements from Multiple Nested Lists")
print(f"First Element : {l2[-1][0]}")
print(f"Last Element : {l2[-1][-1]}")
