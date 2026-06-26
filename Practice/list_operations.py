"""
==========================================================
Lists in Python
==========================================================
Description:
    - A List is used to store multiple values in a single variable.
    - Lists can store different types of data.
    - Lists are ordered and mutable (modifiable).
"""

"""
----------------------------------------------------------
1. Creating a List
----------------------------------------------------------
Description:
    - Creates a list containing different types of data.
Syntax:
    - list_name = [value1, value2, value3]
"""
print("1. Creating a List")
student = ["John", 20, 85.5]
print(f"Student List : {student}")
print("\n")

"""
----------------------------------------------------------
2. Accessing List Elements
----------------------------------------------------------
Description:
    - Access elements using positive and negative indexing.
Syntax:
    - list_name[index]
    - list_name[-index]
"""
print("2. Accessing List Elements")
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Days : {days_of_week}")
print(f"First Day : {days_of_week[0]}")
print(f"Last Day : {days_of_week[-1]}")
print("\n")

"""
----------------------------------------------------------
3. Finding Length of a List
----------------------------------------------------------
Description:
    - Returns the total number of elements in a list.
Syntax:
    - len(list_name)
"""
print("3. Finding Length of a List")
print(f"There are {len(days_of_week)} days in a week")
print("\n")

"""
----------------------------------------------------------
4. List Slicing
----------------------------------------------------------
Description:
    - Extracts a portion of a list.
Syntax:
    - list_name[start:stop]
    - list_name[start:stop:step]
"""
print("4. List Slicing")
l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(f"List : {l1}")
print(f"l1[1:6:1] : {l1[1:6:1]}")
print(f"l1[1:8:20] : {l1[1:8:20]}")
print("\n")

"""
----------------------------------------------------------
5. List Concatenation
----------------------------------------------------------
Description:
    - Joins two or more lists together.
Syntax:
    - list1 + list2
"""
print("5. List Concatenation")
l1 = [1, 7, 2]
l2 = [0, 5]
print(f"List-1 : {l1}")
print(f"List-2 : {l2}")
print(f"l1 + l2 : {l1 + l2}")
print(f"l2 + l1 : {l2 + l1}")
print("\n")

"""
----------------------------------------------------------
6. List Repetition
----------------------------------------------------------
Description:
    - Repeats the list multiple times.
Syntax:
    - list_name * number
"""
print("6. List Repetition")
print(f"List : {l2}")
print(f"Repeated List : {l2 * 3}")
print("\n")

"""
----------------------------------------------------------
7. Smallest Element
----------------------------------------------------------
Description:
    - Returns the smallest value from the list.
Syntax:
    - min(list_name)
"""
print("7. Smallest Element")
numbers = [10, 4, -1, 20, 5.5, 7, 1]
print(f"Numbers : {numbers}")
print(f"Smallest Number : {min(numbers)}")
print("\n")

"""
----------------------------------------------------------
8. Largest Element
----------------------------------------------------------
Description:
    - Returns the largest value from the list.
Syntax:
    - max(list_name)
"""
print("8. Largest Element")
print(f"Numbers : {numbers}")
print(f"Largest Number : {max(numbers)}")
print("\n")

"""
----------------------------------------------------------
9. Sum of List Elements
----------------------------------------------------------
Description:
    - Returns the sum of all numeric elements.
Syntax:
    - sum(list_name)
"""
print("9. Sum of List Elements")
print(f"Numbers : {numbers}")
print(f"Total : {sum(numbers)}")
print("\n")

"""
----------------------------------------------------------
10. Membership Operator (in)
----------------------------------------------------------
Description:
    - Checks whether an element exists in the list.
Syntax:
    - value in list_name
"""
print("10. Membership Operator (in)")
language = ["Python", "Java", "C++"]
print(f"Languages : {language}")
print(f"'Python' in language : {'Python' in language}")
print(f"'JavaScript' in language : {'JavaScript' in language}")
print("\n")

"""
----------------------------------------------------------
11. Membership Operator (not in)
----------------------------------------------------------
Description:
    - Checks whether an element does not exist in the list.
Syntax:
    - value not in list_name
"""
print("11. Membership Operator (not in)")
print(f"Languages : {language}")
print(f"'Python' not in language : {'Python' not in language}")
print(f"'JavaScript' not in language : {'JavaScript' not in language}")
