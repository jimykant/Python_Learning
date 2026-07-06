"""
==========================================================
Dictionary in Python
==========================================================
Description:
    - A dictionary stores data as key-value pairs.
    - Key-value pairs are separated by commas and enclosed within {}.
    - Dictionaries are mutable.
    - Keys must be unique.
    - Syntax:
        {key1: value1, key2: value2, ...}
"""

"""
----------------------------------------------------------
1. Creating a Dictionary
----------------------------------------------------------
Description:
    - Creates a dictionary using key-value pairs.
Syntax:
    - dictionary_name = {key1:value1, key2:value2}
"""
print("1. Creating a Dictionary")
groceries = {"milk": 60, "biscuits": 20, "rice": 90, "bread": 30}
print(f"Dictionary : {groceries}")
print(f"Data Type : {type(groceries)}")
print("\n")

"""
----------------------------------------------------------
2. Finding Length of a Dictionary
----------------------------------------------------------
Description:
    - len() returns the total number of key-value pairs.
Syntax:
    - len(dictionary_name)
"""
print("2. Finding Length of a Dictionary")
print(f"Dictionary : {groceries}")
print(f"Length : {len(groceries)}")
print("\n")

"""
----------------------------------------------------------
3. Accessing Dictionary Values
----------------------------------------------------------
Description:
    - Access a value using its key.
Syntax:
    - dictionary_name[key]
"""
print("3. Accessing Dictionary Values")
print(f"Dictionary : {groceries}")
print(f"Price of Milk : {groceries['milk']}")
print("\n")

"""
----------------------------------------------------------
4. Updating an Existing Value
----------------------------------------------------------
Description:
    - Dictionaries are mutable.
    - If the key exists, its value can be updated.
Syntax:
    - dictionary_name[key] = new_value
"""
print("4. Updating an Existing Value")
print(f"Before Update : {groceries}")
groceries["milk"] = 65
print(f"After Update : {groceries}")
print("\n")

"""
----------------------------------------------------------
5. Adding a New Key-Value Pair
----------------------------------------------------------
Description:
    - If the key does not exist, a new key-value pair is added.
Syntax:
    - dictionary_name[new_key] = value
"""
print("5. Adding a New Key-Value Pair")
print(f"Before Adding : {groceries}")
groceries["eggs"] = 10
print(f"After Adding : {groceries}")
print("\n")

"""
----------------------------------------------------------
6. Accessing Values Using get()
----------------------------------------------------------
Description:
    - get() retrieves the value of a specified key.
    - If the key does not exist, it returns None instead of raising an error.
    - A default value can also be provided.
Syntax:
    - dictionary_name.get(key)
    - dictionary_name.get(key, default_value)
"""
print("6. Accessing Values Using get()")
student1 = {"maths": 80.5, "eng": 76.0, "phy": 89.0}
print(f"Dictionary : {student1}")
print(f"Physics Marks : {student1['phy']}")
print(f"student1.get('phy') : {student1.get('phy')}")
print(f"student1.get('chem') : {student1.get('chem')}")
print(f"student1.get('chem', 40.0) : {student1.get('chem', 40.0)}")
print(f"Dictionary After get() : {student1}")
print("\n")

"""
----------------------------------------------------------
7. Membership Operators in Dictionary
----------------------------------------------------------
Description:
    - Membership operators check only keys, not values.
    - 'in' returns True if the key exists.
    - 'not in' returns True if the key does not exist.
Syntax:
    - key in dictionary_name
    - key not in dictionary_name
"""
print("7. Membership Operators in Dictionary")
emp1 = {"id": 1001, "name": "John", "salary": 10000}
print(f"Dictionary : {emp1}")
print(f"1001 in emp1 : {1001 in emp1}")
print(f"'name' in emp1 : {'name' in emp1}")
print("\n")

"""
----------------------------------------------------------
8. Updating a Dictionary
----------------------------------------------------------
Description:
    - update() adds all key-value pairs from another dictionary.
    - If a key already exists, its value is updated.
Syntax:
    - dictionary_name.update(other_dictionary)
"""
print("8. Updating a Dictionary")
sem1_marks = {"maths": 78.5, "eng": 71.0, "phy": 86.5}
sem2_marks = {"chem": 81.5, "bio": 90.5, "eng": 70.0}
print(f"Semester 1 Marks : {sem1_marks}")
print(f"Semester 2 Marks : {sem2_marks}")
sem1_marks.update(sem2_marks)
print(f"Updated Dictionary : {sem1_marks}")
print("\n")

"""
----------------------------------------------------------
9. Removing a Key-Value Pair
----------------------------------------------------------
Description:
    - pop() removes a specified key-value pair.
    - It returns the removed value.
Syntax:
    - dictionary_name.pop(key)
"""
print("9. Removing a Key-Value Pair")
print(f"Before pop() : {sem1_marks}")
sem1_marks.pop("phy")
print(f"After pop() : {sem1_marks}")
print("\n")

"""
----------------------------------------------------------
10. Duplicate Keys in Dictionary
----------------------------------------------------------
Description:
    - Dictionary keys must be unique.
    - If duplicate keys are provided, the last value is retained.
Syntax:
    - {key:value1, key:value2}
"""
print("10. Duplicate Keys in Dictionary")
groceries = {"milk": 60, "rice": 100, "biscuits": 20, "milk": 65}
print(f"Dictionary : {groceries}")
print("The last value of 'milk' is retained.")
print("\n")

"""
----------------------------------------------------------
11. Valid Dictionary Keys
----------------------------------------------------------
Description:
    - Dictionary keys must be "Immutable" (hashable) data types.
    - Immutable objects can be used as keys because their values do not change.
    - Mutable objects cannot be used as keys.
Syntax:
    - {key: value}
Note:
    - Valid Keys : str, int, float, bool, tuple (Immutable)
    - Invalid Keys : list, set, dictionary (Mutable)
"""
print("11. Valid Dictionary Keys")
# Valid Keys (String)
d1 = {"Nine": 9, "Four": 4}
print(f"String Keys : {d1}")
# (Integer)
d1 = {1: True, 0: False}
print(f"Integer Keys : {d1}")
# (Float)
d1 = {1.0: True, 0.0: False}
print(f"Float Keys : {d1}")
# (Boolean)
d1 = {True: 1, False: 0}
print(f"Boolean Keys : {d1}")
# (Tuple)
d1 = {(1, 3, 5): 9, (2, 2): 4}
print(f"Tuple Keys : {d1}")
print("\n")

"""
----------------------------------------------------------
12. Invalid Dictionary Keys
----------------------------------------------------------
Description:
    - Mutable data types cannot be used as dictionary keys.
    - Using them as keys raises a TypeError.
Syntax:
    - Invalid: {list: value}
    - Invalid: {set: value}
    - Invalid: {dictionary: value}
"""
print("12. Invalid Dictionary Keys")
print("List[], Set{}, and Dictionary{key: value} cannot be used as keys.")
print("They raise a TypeError because they are 'Mutable'.")
print("\n")

"""
----------------------------------------------------------
13. Dictionary Values Can Be Any Data Type
----------------------------------------------------------
Description:
    - Dictionary values can store any type of data.
    - Values can be numbers, strings, lists, tuples, sets, or even another dictionary.
Syntax:
    - {key: value}
"""
print("13. Dictionary Values Can Be Any Data Type")
student1 = {
    "id": 100,
    "name": "John",
    "marks": {
        "eng": 89.5,
        "maths": 71.5,
        "bio": 81.0
    },
    "subjects": ["eng", "maths", "bio"]
}
print(f"Dictionary : {student1}")
print("\n")

"""
----------------------------------------------------------
14. Accessing Nested Dictionary Values
----------------------------------------------------------
Description:
    - A dictionary can contain another dictionary as a value.
    - Multiple indexing operations can be used to access nested values.
Syntax:
    - dictionary[key1][key2]
"""
print("14. Accessing Nested Dictionary Values")
print(f"Dictionary : {student1}")
print(f"Getting 'Marks' Dictionary : {student1['marks']}")
print(f"Getting 'Maths' score from 'Marks' Dictionary  : {student1['marks']['maths']}")
print("\n")

"""
----------------------------------------------------------
15. Accessing List Values Inside a Dictionary
----------------------------------------------------------
Description:
    - A dictionary value can also be a list.
    - List indexing can be used after accessing the list.
Syntax:
    - dictionary[key][index]
"""
print("15. Accessing List Values Inside a Dictionary")
print(f"Dictionary : {student1}")
print(f"Getting 'Subjects' List : {student1['subjects']}")
print(f"Getting First 'Subject' from above List : {student1['subjects'][0]}")
print("\n")

"""
----------------------------------------------------------
16. Fetching All Keys
----------------------------------------------------------
Description:
    - keys() returns all keys of a dictionary.
    - The returned object is of type dict_keys.
Syntax:
    - dictionary.keys()
"""
print("16. Fetching All Keys")
print(f"Dictionary : {student1}")
print(f"Keys : {student1.keys()}")
print(f"Data Type : {type(student1.keys())}")
print("\n")

"""
----------------------------------------------------------
17. Fetching All Values
----------------------------------------------------------
Description:
    - values() returns all values of a dictionary.
    - The returned object is of type dict_values.
Syntax:
    - dictionary.values()
"""
print("17. Fetching All Values")
print(f"Dictionary : {student1}")
print(f"Values : {student1.values()}")
print(f"Data Type : {type(student1.values())}")
print("\n")

"""
----------------------------------------------------------
18. Fetching Keys and Values Together
----------------------------------------------------------
Description:
    - items() returns both keys and values.
    - Each key-value pair is returned as a tuple.
    - The returned object is of type dict_items.
Syntax:
    - dictionary.items()
"""
print("18. Fetching Keys and Values Together")
print(f"Dictionary : {student1}")
print(f"Items : {student1.items()}")
print(f"Data Type : {type(student1.items())}")
