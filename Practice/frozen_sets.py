"""
==========================================================
Frozen Sets in Python
==========================================================
Description:
    - A Frozen Set is an immutable version of a set.
    - Once created, elements cannot be added, removed, or modified.
    - Frozen sets support all read-only set operations like intersection, union, and difference.
"""

"""
----------------------------------------------------------
1. Creating a Frozen Set
----------------------------------------------------------
Description:
    - Creates an immutable (read-only) set.
Syntax:
    - frozenset(iterable)
Note:
    - Since frozen sets are immutable, methods like add(), remove(), discard(), clear(), etc. are not supported.
"""
print("1. Creating a Frozen Set")
fs1 = frozenset({10, 20, 30})
fs2 = frozenset({10, 50, 100, 200})
print(f"Frozen Set 1 : {fs1} {type(fs1)}")
print(f"Frozen Set 2 : {fs2} {type(fs2)}")
print("\n")

"""
----------------------------------------------------------
2. Intersection Operation on Frozen Sets
----------------------------------------------------------
Description:
    - Returns the common elements present in both frozen sets.
Syntax:
    - fs1 & fs2
    - fs1.intersection(fs2)
Note:
    - A new frozen set is returned because frozen sets cannot be modified.
"""
print("2. Intersection Operation on Frozen Sets")
common_elements = fs1 & fs2
# OR common_elements = fs1.intersection(fs2)
print(f"Frozen Set 1 : {fs1}")
print(f"Frozen Set 2 : {fs2}")
print(f"Common Elements : {common_elements}")
print("\n")

"""
----------------------------------------------------------
3. Union Operation on Frozen Sets
----------------------------------------------------------
Description:
    - Returns all unique elements from both frozen sets.
Syntax:
    - fs1 | fs2
    - fs1.union(fs2)
Note:
    - Duplicate elements are automatically removed.
"""
print("3. Union Operation on Frozen Sets")
all_elements = fs1 | fs2
# OR all_elements = fs1.union(fs2)
print(f"Frozen Set 1 : {fs1}")
print(f"Frozen Set 2 : {fs2}")
print(f"All Elements : {all_elements}")
print("\n")

"""
----------------------------------------------------------
4. Difference Operation on Frozen Sets
----------------------------------------------------------
Description:
    - Returns the elements that are present in the first frozen set
      but NOT present in the second frozen set.
Syntax:
    - fs1 - fs2
    - fs1.difference(fs2)
Note:
    - Difference is not commutative.
    - fs1 - fs2 is different from fs2 - fs1.
"""
print("4. Difference Operation on Frozen Sets")
difference_elements_1 = fs1 - fs2
difference_elements_2 = fs2 - fs1
# OR difference_elements = fs1.difference(fs2)
print(f"Frozen Set 1 : {fs1}")
print(f"Frozen Set 2 : {fs2}")
print(f"Difference Elements fs1 - fs2: {difference_elements_1}")
print(f"Difference Elements fs2 - fs1: {difference_elements_2}")
