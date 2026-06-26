"""
==========================================================
String Indexing & Slicing in Python
==========================================================
Description:
    - Indexing is used to access a single character from a string.
    - Slicing is used to extract a portion of a string.
    - Strings are immutable, so indexing and slicing only retrieve data.
"""

"""
----------------------------------------------------------
1. String Indexing
----------------------------------------------------------
Description:
    - Access a single character using its index position.
    - Positive indexing starts from 0.
    - Negative indexing starts from -1.
Syntax:
    - string[index]
"""
print("1. String Indexing")
str1 = "Hello World"
print(f"String : {str1}")
print(f"First Character : {str1[0]}")
print(f"Last Character : {str1[-1]}")
print("\n")

"""
----------------------------------------------------------
2. String Slicing
----------------------------------------------------------
Description:
    - Extract a portion of a string.
    - The start index is included, but the end index is excluded.
Syntax:
    - string[start_index:end_index]
"""
print("2. String Slicing")
print(f"String : {str1}")
print(f"str1[1:5] : {str1[1:5]}")
print("\n")

"""
----------------------------------------------------------
3. String Slicing with Step
----------------------------------------------------------
Description:
    - Extract characters by skipping elements using the step value.
Syntax:
    - string[start_index:end_index:step]
"""
print("3. String Slicing with Step")
print(f"str1[2:7:2] : {str1[2:7:2]}")
print(f"str1[2:9:2] : {str1[2:9:2]}")
print(f"str1[1:12:3] : {str1[1:12:3]}")
print(f"str1[1:5:1] : {str1[1:5:1]}")
