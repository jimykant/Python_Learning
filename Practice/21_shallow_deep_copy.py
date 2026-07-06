"""
==========================================================
Shallow Copy and Deep Copy in Python
==========================================================
Description:
    - Copying creates a new object from an existing object.
    - Python provides two types of copying:
        1. Shallow Copy
        2. Deep Copy
"""

import copy

"""
----------------------------------------------------------
1. Shallow Copy
----------------------------------------------------------
Description:
    - Creates a new outer object.
    - Nested objects are shared between the original and copied object.
    - Changes to nested objects affect both lists.
Syntax:
    - copy.copy(object)
"""
print("1. Shallow Copy")
l1 = [1, 2.5, [10, 20, 30], "Python"]
print(f"Original List : {l1} and ID : {id(l1)}")
l2 = copy.copy(l1)
print(f"Copied List : {l2} and ID : {id(l2)}")

# Changing a normal element
# l1[0] = 100 affects only l1 because the value is replaced.
l1[0] = 100
print(f"After l1[0] = 100")
print(f"l1 : {l1}")
print(f"l2 : {l2}")

# Changing a nested element
# l1[2][0] = 50 affects both lists because the nested list is shared.
l1[2][0] = 50
print(f"After l1[2][0] = 50")
print(f"l1 : {l1}")
print(f"l2 : {l2}")
print("\n")

"""
----------------------------------------------------------
2. Deep Copy
----------------------------------------------------------
Description:
    - Creates a completely independent copy.
    - Both outer and nested objects are copied.
    - Changes in one object do not affect the other.
Syntax:
    - copy.deepcopy(object)
"""
print("2. Deep Copy")
l1 = [1, 2.5, [10, 20, 30], "Python"]
print(f"Original List : {l1} and ID : {id(l1)}")
l2 = copy.deepcopy(l1)
print(f"Copied List : {l2} and ID : {id(l2)}")

# Changing a normal element
# l1[0] = 100 affects only l1.
l1[0] = 100
print(f"After l1[0] = 100")
print(f"l1 : {l1}")
print(f"l2 : {l2}")

# Changing a nested element
# l1[2][0] = 50 also affects only l1.
l1[2][0] = 50
print(f"After l1[2][0] = 50")
print(f"l1 : {l1}")
print(f"l2 : {l2}")
