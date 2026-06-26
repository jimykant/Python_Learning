"""
==========================================================
Let's see some Operations on Set
==========================================================
"""

"""
----------------------------------------------------------
1. Membership Operators in Set
----------------------------------------------------------
Description:
    - Membership operators are used to check whether an element exists in the set or not.
Syntax:
    - element in set
    - element not in set
Note:
    - Returns True if the element is present in the set; otherwise, returns False.
"""
print("1. Membership Operators in Set - in, not in")
nums = {1, 3, 2, 0, -1}
print(f"Set is: {nums}")
print(f"Is 0 present in the set? {0 in nums}")
print(f"Is 10 present in the set? {10 in nums}")
print(f"Is 0 not present in the set? {0 not in nums}")
print(f"Is 10 not present in the set? {10 not in nums}")
print("\n")

"""
----------------------------------------------------------
2. Tuple to Set Conversion
----------------------------------------------------------
Description:
    - Converts a tuple into a set.
Syntax:
    - set(tuple)
Note:
    - Duplicate elements are automatically removed during conversion.
"""
print("2. Tuple to Set Conversion - set(tuple)")
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(f"Original Tuple : {weekdays}")
weekdays_set = set(weekdays)
print(f"Converted Set : {weekdays_set}")
print("\n")

"""
----------------------------------------------------------
3. Set to Tuple and List Conversion
----------------------------------------------------------
Description:
    - Converts a set into a tuple or a list.
Syntax:
    - tuple(set)
    - list(set)
Note:
    - Since sets are unordered, the order of elements in the tuple or list may be different each time.
"""
print("3. Set to Tuple and List Conversion")
set1 = {"Python", "Java", "C++", "C"}
print(f"Original Set : {set1}")
tuple1 = tuple(set1)
list1 = list(set1)
print(f"Tuple : {tuple1}")
print(f"List : {list1}")
print("\n")

"""
----------------------------------------------------------
4. add() Method
----------------------------------------------------------
Description:
    - Adds a new element to the set. Sets are mutable, so elements can be added or removed after creation.
Syntax:
    - set.add(element)
Note:
    - If the element already exists, it is not added again because sets store only unique elements.
"""
print("4. add() Method")
set1 = {2, 0, -1}
print(f"Original Set : {set1}")
set1.add(5)
print(f"Set after adding 5 : {set1}")
print("\n")

"""
----------------------------------------------------------
5. remove() Method
----------------------------------------------------------
Description:
    - Removes the specified element from the set.
Syntax:
    - set.remove(element)
Note:
    - If the element is not present in the set, Python raises a KeyError.
"""
print("5. remove() Method")
set1 = {2, 0, -1}
print(f"Original Set : {set1}")
set1.remove(0)
print(f"Set after removing 0 : {set1}")
print("\n")

"""
----------------------------------------------------------
6. discard() Method
----------------------------------------------------------
Description:
    - Removes the specified element from the set.
Syntax:
    - set.discard(element)
Note:
    - If the element is not present in the set, discard() does not generate any error.
"""
print("6. discard() Method")
set1 = {2, 0, -1}
print(f"Original Set : {set1}")
set1.discard(0)
print(f"Set after discarding 0 : {set1}")
# Trying to discard an element that does not exist
set1.discard(100)
print(f"After discarding 100 : {set1}")
print("\n")

"""
==========================================================
Mathematical Operations on Sets
==========================================================
Description:
    - Python provides various mathematical operations that can be performed on sets.
    - These operations include:
        1. Intersection
        2. Union
        3. Difference
"""
print("# Let's see some Mathematical Operations on Sets")
"""
----------------------------------------------------------
1. Intersection Operation
----------------------------------------------------------
Description:
    - Returns the common elements present in both sets.
Syntax:
    - set1 & set2
    - set1.intersection(set2)
Note:
    - Only the elements that exist in both sets are returned.
"""
print("1. Intersection Operation")
student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
common_subjects = student1 & student2
# OR common_subjects = student1.intersection(student2)
print(f"Student 1 Subjects : {student1}")
print(f"Student 2 Subjects : {student2}")
print(f"Common Subjects : {common_subjects}")
print("\n")

"""
----------------------------------------------------------
2. Union Operation
----------------------------------------------------------
Description:
    - Returns all unique elements from two or more sets.
Syntax:
    - set1 | set2
    - set1.union(set2)
Note:
    - Get all both the sets elements but, Duplicate elements are automatically removed.
"""
print("2. Union Operation")
student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}
all_subjects = student1 | student2 | student3
# OR all_subjects = student1.union(student2, student3)
print(f"Student 1 Subjects : {student1}")
print(f"Student 2 Subjects : {student2}")
print(f"Student 3 Subjects : {student3}")
print(f"All Subjects : {all_subjects}")
print("\n")

"""
----------------------------------------------------------
3. Difference Operation
----------------------------------------------------------
Description:
    - Returns the elements that are present in the first set
      but NOT present in the second set.
Syntax:
    - set1 - set2
    - set1.difference(set2)
Note:
    - Difference is not commutative.
    - set1 - set2 is different from set2 - set1.
"""
print("3. Difference Operation")
days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}
weekdays = days - weekends
# OR weekdays = days.difference(weekends)
print(f"Days : {days}")
print(f"Weekends : {weekends}")
print(f"Working Days : {weekdays}")
