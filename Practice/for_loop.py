"""
==========================================================
For Loop in Python
==========================================================
Description:
    - A for loop is used to iterate over a sequence.
    - It executes a block of code once for each item in the sequence.
    - Commonly used with lists, strings, tuples, and range().
"""

"""
----------------------------------------------------------
1. Iterating Through a List
----------------------------------------------------------
Description:
    - The loop visits each element of the list one by one.
Syntax:
    - for variable in sequence:
          statement
"""
print("1. Iterating Through a List")
l1 = ["Mike", 10.2, 1980]
print(f"List : {l1}")
for i in l1:
    print(i)
print("\n")

"""
----------------------------------------------------------
2. Iterating Through a List Directly
----------------------------------------------------------
Description:
    - A list can be provided directly inside the loop.
Syntax:
    - for variable in [item1, item2, item3]:
          statement
"""
print("2. Iterating Through a List Directly")
for i in ["Mike", 10.2, 1980]:
    print(i)
print("\n")

"""
----------------------------------------------------------
3. Iterating Through a String
----------------------------------------------------------
Description:
    - The loop visits each character of the string one by one.
Syntax:
    - for variable in string:
          statement
"""
print("3. Iterating Through a String")
x = "Apple"
for i in x:
    print(i)
print("\n")

"""
----------------------------------------------------------
4. Using range()
----------------------------------------------------------
Description:
    - range() generates a sequence of numbers.
    - range(start, stop) generates numbers from start to stop-1.
Syntax:
    - range(start, stop)
"""
print("4. Using range()")
for i in range(1, 11):
    print(i)
print("\n")

"""
----------------------------------------------------------
5. Repeating a Statement Multiple Times
----------------------------------------------------------
Description:
    - range() can be used to repeat an action a specific number of times.
Syntax:
    - for variable in range(start, stop):
          statement
"""
print("5. Repeating a Statement Multiple Times")
for i in range(1, 3):
    print("Apple")
