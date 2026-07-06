"""
==========================================================
Tuples in Python
==========================================================
Description:
    - A tuple is an ordered collection of elements.
    - Tuple elements are enclosed within parentheses ().
    - A tuple can store elements of different data types.
    - Tuples are immutable, which means their elements cannot be modified after creation.
"""

"""
----------------------------------------------------------
1. Creating a Tuple and Finding Length
----------------------------------------------------------
Description:
    - Creates a tuple containing different types of elements.
    - len() returns the total number of elements in a tuple.
Syntax:
    - tuple_name = (element1, element2, ...)
    - len(tuple_name)
"""
print("1. Creating a Tuple and Finding Length")
t1 = ("Python", 10, 1.5, True, [1, 2, 3], (10, 20))
print(f"Tuple : {t1}")
print(f"Length : {len(t1)}")
print("\n")

"""
----------------------------------------------------------
2. Tuple Indexing
----------------------------------------------------------
Description:
    - Access individual elements using positive or negative indexing.
Syntax:
    - tuple_name[index]
"""
print("2. Tuple Indexing")
print(f"First Element : {t1[0]}")
print(f"Last Element : {t1[-1]}")
print("\n")

"""
----------------------------------------------------------
3. Tuple Slicing
----------------------------------------------------------
Description:
    - Extract a portion of a tuple.
Syntax:
    - tuple_name[start_index:end_index:step]
"""
print("3. Tuple Slicing")
print(f"Sliced Tuple : {t1[1:5:2]}")
print("\n")

"""
----------------------------------------------------------
4. Creating a Tuple Without Parentheses
----------------------------------------------------------
Description:
    - Parentheses are optional while creating a tuple.
Syntax:
    - tuple_name = value1, value2, value3
"""
print("4. Creating a Tuple Without Parentheses")
t2 = 10, 20, 30
print(f"Tuple : {t2}")
print(f"Data Type : {type(t2)}")
print("\n")

"""
----------------------------------------------------------
5. Converting List to Tuple
----------------------------------------------------------
Description:
    - tuple() converts a list into a tuple.
Syntax:
    - tuple(list_name)
"""
print("5. Converting List to Tuple")
l1 = [1, 2, 3]
print(f"Original List : {l1}")
print(f"Data Type : {type(l1)}")
t3 = tuple(l1)
print(f"Converted Tuple : {t3}")
print(f"Data Type : {type(t3)}")
print("\n")

"""
----------------------------------------------------------
6. Converting Tuple to List
----------------------------------------------------------
Description:
    - list() converts a tuple into a list.
Syntax:
    - list(tuple_name)
"""
print("6. Converting Tuple to List")
fruits = ("Mango", "Orange", "Apple")
print(f"Original Tuple : {fruits}")
print(f"Data Type : {type(fruits)}")
fruits = list(fruits)
print(f"Converted List : {fruits}")
print(f"Data Type : {type(fruits)}")
print("\n")

"""
----------------------------------------------------------
7. Tuple Concatenation
----------------------------------------------------------
Description:
    - Concatenation joins two tuples into one tuple.
Syntax:
    - tuple1 + tuple2
"""
print("7. Tuple Concatenation")
std1 = (1001, "John")
std2 = (78.5, 91.0, 83.5, 79.5)
print(f"Student Detail 1 : {std1}")
print(f"Student Detail 2 : {std2}")
student_details = std1 + std2
print(f"Combined Tuple : {student_details}")
print("\n")

"""
----------------------------------------------------------
8. Tuple Repetition
----------------------------------------------------------
Description:
    - Repeats the tuple a specified number of times.
Syntax:
    - tuple_name * integer
"""
print("8. Tuple Repetition")
t1 = ("Class5", 5000)
print(f"Original Tuple : {t1}")
print(f"Repeated Tuple : {t1 * 3}")
print("\n")

"""
----------------------------------------------------------
9. Membership Operators
----------------------------------------------------------
Description:
    - 'in' checks whether an element exists in the tuple.
    - 'not in' checks whether an element does not exist in the tuple.
Syntax:
    - element in tuple_name
    - element not in tuple_name
"""
print("9. Membership Operators")
print(f"Tuple : {std2}")
print(f"91.0 in std2 : {91.0 in std2}")
print(f"99.0 in std2 : {99.0 in std2}")
print(f"91.0 not in std2 : {91.0 not in std2}")
print(f"99.0 not in std2 : {99.0 not in std2}")
print("\n")

"""
----------------------------------------------------------
10. Counting Elements
----------------------------------------------------------
Description:
    - count() returns the number of occurrences of an element.
Syntax:
    - tuple_name.count(element)
"""
print("10. Counting Elements")
t1 = (10, 4, 1, 9, 0, 1, 1, 1, 0, 1, "Python")
print(f"Tuple : {t1}")
print(f"Occurrences of 1 : {t1.count(1)}")
print("\n")

"""
----------------------------------------------------------
11. Finding Index of an Element
----------------------------------------------------------
Description:
    - index() returns the index of the first occurrence of an element.
Syntax:
    - tuple_name.index(element)
"""
print("11. Finding Index of an Element")
print(f"Tuple : {t1}")
print(f"Index of 1 : {t1.index(1)}")
print(f"Index of 'Python' : {t1.index('Python')}")
print("\n")

"""
----------------------------------------------------------
12. Finding Minimum Value
----------------------------------------------------------
Description:
    - min() returns the smallest element from a tuple.
Syntax:
    - min(tuple_name)
"""
print("12. Finding Minimum Value")
t1 = (10, 4, 1, 9, 0, 3, 1)
print(f"Tuple : {t1}")
print(f"Minimum Value : {min(t1)}")
print("\n")

"""
----------------------------------------------------------
13. Finding Maximum Value
----------------------------------------------------------
Description:
    - max() returns the largest element from a tuple.
Syntax:
    - max(tuple_name)
"""
print("13. Finding Maximum Value")
print(f"Tuple : {t1}")
print(f"Maximum Value : {max(t1)}")
print("\n")

"""
----------------------------------------------------------
14. Sum of Tuple Elements
----------------------------------------------------------
Description:
    - sum() returns the total of all numeric elements in a tuple.
Syntax:
    - sum(tuple_name)
"""
print("14. Sum of Tuple Elements")
print(f"Tuple : {t1}")
print(f"Total Sum : {sum(t1)}")
