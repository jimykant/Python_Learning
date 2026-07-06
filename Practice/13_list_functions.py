"""
==========================================================
Functions of List
==========================================================
Description:
    - Python provides many built-in functions (methods) to modify,
      access, and manage list elements.
    - These functions make working with lists easy and efficient.
"""

"""
----------------------------------------------------------
1. append()
----------------------------------------------------------
Description:
    - Adds only one item to the end of the list.
Syntax:
    - list_name.append(item)
"""
print("1. append() - Add a Single Item to the End of the List")
fruits = ["Mango", "Apple", "Orange"]
print(f"Original Fruit List : {fruits}")
fruits.append("Banana")
print(f"Updated Fruit List  : {fruits}")
print("\n")

"""
----------------------------------------------------------
2. insert()
----------------------------------------------------------
Description:
    - Inserts one item before the specified index.
Syntax:
    - list_name.insert(index, item)
"""
print("2. insert() - Insert Item at a Specific Position")
print(f"Current Fruit List : {fruits}")
fruits.insert(2, "Pineapple")
print(f"Updated Fruit List : {fruits}")
print("\n")

"""
----------------------------------------------------------
3. extend()
----------------------------------------------------------
Description:
    - Adds multiple items to the end of the list.
Syntax:
    - list_name.extend([item1, item2, ...])
"""
print("3. extend() - Add Multiple Items")
print(f"Current Fruit List : {fruits}")
fruits.extend(["Grapes", "Cherry"])
print(f"Updated Fruit List : {fruits}")
print("\n")

"""
----------------------------------------------------------
4. remove()
----------------------------------------------------------
Description:
    - Removes the first matching item from the list.
Syntax:
    - list_name.remove(item)
Note:
    - Raises an error if the item is not found.
"""
print("4. remove() - Remove an Item")
print(f"Current Fruit List : {fruits}")
fruits.remove("Banana")
print(f"Updated Fruit List : {fruits}")
print("\n")

"""
----------------------------------------------------------
5. pop()
----------------------------------------------------------
Description:
    - Removes an item using its index.
    - If no index is provided, it removes the last item.
Syntax:
    - list_name.pop(index)
    - list_name.pop()
"""
print("5. pop() - Remove Item Using Index")
print(f"Current Fruit List : {fruits}")
fruits.pop(3)
print(f"Updated Fruit List : {fruits}")
print("\n")

"""
----------------------------------------------------------
6. reverse()
----------------------------------------------------------
Description:
    - Reverses the order of list elements.
Syntax:
    - list_name.reverse()
"""
print("6. reverse() - Reverse List")
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
print(f"Original Days List : {days_of_week}")
days_of_week.reverse()
print(f"Reversed Days List : {days_of_week}")
print("\n")

"""
----------------------------------------------------------
7. sort()
----------------------------------------------------------
Description:
    - Sorts the list.
    - By default, it sorts in ascending order.
Syntax:
    - list_name.sort()
    - list_name.sort(reverse=True)
"""
print("7. sort() - Sort List")
nums = [4, 9, 1, 8, 0, 2]
print(f"Original Number List : {nums}")
nums.sort()
print(f"Ascending Order      : {nums}")
nums.sort(reverse=True)
print(f"Descending Order     : {nums}")
print("\n")

"""
----------------------------------------------------------
8. count()
----------------------------------------------------------
Description:
    - Counts how many times a specific item appears.
Syntax:
    - list_name.count(item)
"""
print("8. count() - Count Occurrence of an Item")
nums = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"Number List : {nums}")
item_to_count = int(input("Enter the number to count: "))
print(f"{item_to_count} appears {nums.count(item_to_count)} time(s).")
