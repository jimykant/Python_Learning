"""
==========================================================
Delete Dictionary Items Using for Loop
==========================================================
Description:
    - Delete dictionary items using a for loop.
    - Useful for removing sensitive information.
"""

"""
----------------------------------------------------------
1. Delete Existing Keys from Dictionary
----------------------------------------------------------
Description:
    - Delete sensitive information from a dictionary.
Syntax:
    - for variable in iterable:
          dictionary.pop(key)
Note:
    - pop(key) removes the key-value pair.
    - Raises KeyError if the key does not exist.
"""
print("1. Delete Existing Keys from Dictionary")
user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}
sensitive_info = ["password", "address"]
for i in sensitive_info:
    print(f"DELETED => key: {i}, value: {user[i]}")
    user.pop(i)
print("Remaining Dictionary:")
print(user)
print("\n")

"""
----------------------------------------------------------
2. Delete Keys Safely (Handle Missing Keys)
----------------------------------------------------------
Description:
    - Check whether a key exists before deleting it.
Syntax:
    - if key in dictionary:
          dictionary.pop(key)
      else:
          # Key not found
Note:
    - Prevents KeyError.
    - Useful when some keys may not exist.
"""
print("2. Delete Keys Safely (Handle Missing Keys)")
user1 = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}
sensitive_info1 = ["password", "address", "phone"]
for i in sensitive_info1:
    if i in user1:
        print(f"DELETED => key: {i}, value: {user1[i]}")
        user1.pop(i)
    else:
        print(f"'{i}' is not in user dictionary")
print("Remaining Dictionary:")
print(user1)
