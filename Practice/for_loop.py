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
    - range(start, stop, step) generates numbers from 'start' to 'stop-1'.
    - A negative step generates numbers in reverse order.
Syntax:
    - range(start, stop, step)
"""
print("4. Using range()")
# Forward Order (Positive step)
print("Forward Order")
for i in range(1, 11, 2):
    print(i)
print("\n")
# Reverse Order (Negative step)
print("Reverse Order")
for i in range(20, 10, -2):
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
print("\n")

"""
----------------------------------------------------------
6. Iterating Through a Dictionary
----------------------------------------------------------
Description:
    - A for loop can be used to iterate through a dictionary.
    - By default, a dictionary loop returns only the keys.
    - keys() returns all keys.
    - values() returns all values.
    - items() returns both keys and values.
Syntax:
    - for key in dictionary:
          statement

    - for key in dictionary.keys():
          statement

    - for value in dictionary.values():
          statement

    - for key, value in dictionary.items():
          statement
"""
print("6. Iterating Through a Dictionary")

employee = {
    "empid": 1001,
    "name": "John Gray",
    "department": "HR"
}

print("Dictionary :")
print(employee)
print("\n")
# Fetching Only Keys
print("1. Fetching Only Keys")
for key in employee:
    print(key)
print("\n")
# Fetching Only Values
print("2. Fetching Only Values")
for value in employee.values():
    print(value)
print("\n")
# Fetching Both Keys and Values
print("3. Fetching Both Keys and Values")
for key, value in employee.items():
    print(f"{key} : {value}")
print("\n")

"""
----------------------------------------------------------
7. Finding Sum Using for Loop
----------------------------------------------------------
Description:
    - A for loop can be used to calculate the total of all elements.
    - This works similarly to the sum() function.
Syntax:
    - total = 0
    - for item in sequence:
          total = total + item
"""
print("7. Finding Sum Using for Loop")
scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
print(f"Scores : {scores}")
total = 0
for score in scores:
    total = total + score
print(f"Total Score : {total}")
print("\n")

"""
----------------------------------------------------------
8. Finding Highest Value Using for Loop
----------------------------------------------------------
Description:
    - A for loop can be used to find the largest value in a sequence.
    - This works similarly to the max() function.
Syntax:
    - highest = sequence[0]
    - for item in sequence:
          if highest < item:
              highest = item
"""
print("8. Finding Highest Value Using for Loop")
print(f"Scores : {scores}")
highest = scores[0] # assumed that the 1st value of list is highest
for score in scores:
    if highest < score:
        highest = score
print(f"Highest Score : {highest}")
