"""
# Tuple :- It is also the comma separated elements in close within parenthesis'()' or without it '()'
# Example :- (item1, item2, item3)
# Sequence of the items as a collection
# It stores elements of any data-type
# The elements of it is fixed we can not change it means can not do (append, remove, etc...)
"""
# Length of the tuple - len()
print("# Let's see some Operations on a Tuple")
print("1. Length of the tuple - len()")
t1 = ("Python", 10, 1.5, True, [1, 2, 3], (10, 20))
print(f"Tuple is: {t1}")
print(f"Length of the given tuple is: {len(t1)}")
print("\n")

# Accessing the Tuple elements - using Indexing
# Syntax - tuple[index]
print("2. Indexing - tuple[index]")
print(f"The First element of the tuple is: {t1[0]}")
print(f"The Last element of the tuple is: {t1[-1]}")
print("\n")

# Slicing in the tuple
# Syntax - tuple[start-index:end-index:step]
print("3. Slicing - tuple[start-index:end-index:step]")
print(f"Slicing of the tuple: {t1[1:5:2]}")
print("\n")

# Type of tuple
t2 = 10, 20, 30
print(f"Another Tuple is: {t2}")
print(f"Type of it: {type(t2)}")
print("\n")

# Convert list to tuple - tuple(list)
print("4. Convert list to tuple - tuple(list)")
l1 = [1, 2, 3]
print(f"This is list {l1} is {type(l1)}")
t1 = tuple(l1)
print(f"List is converted to Tuple {t1} is {type(t1)}")
print("\n")

# Convert tuple to list - list(tuple)
print("5. Convert tuple to list - list(tuple)")
fruits = "Mango", "Orange", "Apple"
print(f"This is tuple {fruits} is {type(fruits)}")
fruits = list(fruits)
print(f"Tuple is converted to List {fruits} is {type(fruits)}")
print("\n")

# Concatenation of tuple
print("6. Concatenation of tuple - +")
std1 = (1001, "John")
print(f"student_detail_1 is: {std1}")
std2 = (78.5, 91.0, 83.5, 79.5)
print(f"student_detail_2 is: {std2}")
student_details = std1 + std2
print(f"Entire details is: {student_details}")
print("\n")

# Repetition of tuple - *
print("7. Repetition of tuple - *")
t1 = ("class5", 5000)
print(f"Initial tuple is: {t1}")
print(f"Repetition: {t1 * 3}")
print("\n")

# Membership operation in tuple - 'in' and 'not in'
print("8. Membership operation in tuple - 'in' and 'not in'")
print(f"student_detail_2 is: {std2}")
print(91.0 in std2)
print(99.0 in std2)
print(91.0 not in std2)
print(99.0 not in std2)
print("\n")

# Count operation on tuple - tuple.count(element)
print("9. Count operation on tuple - tuple.count(element)")
t1 = (10, 4, 1, 9, 0, 1, 1, 1, 0, 1, "Python")
print(f"Tuple is: {t1}")
print (f"Occurrence of '1' in above tuple is: {t1.count(1)}")
print("\n")

# Index Operation - it gives the index of the element of the tuple
# Syntax - tuple.index(element)
print("10. Index Operation - it gives the index of the element of the tuple - tuple.index(element)")
print(f"Tuple is: {t1}")
print(f"Index of the '1' is {t1.index(1)}")  # what is the index of the '1' in above tuple ?
print(f"Index of the 'Python' is: {t1.index('Python')}")
print("\n")

# Minimum Value - it gives the smallest value in the tuple
# Syntax - min(tuple)
print("11. Minimum Value - smallest value in the tuple - min(tuple)")
t1 = (10, 4, 1, 9, 0, 3, 1)
print(f"Tuple is: {t1}")
print(f"Smallest value in the tuple is: {min(t1)}")
print("\n")

# Maximum Value - it gives the largest value in the tuple
# Syntax - max(tuple)
print("12. Maximum Value - largest value in the tuple - max(tuple)")
print(f"Tuple is: {t1}")
print(f"Largest value in the tuple is: {max(t1)}")
print("\n")


# Sum of Tuple - it gives the total sum of all elements in the tuple
# Syntax - sum(tuple)
print("13. Sum of Tuple - total sum of all elements in the tuple - sum(tuple)")
print(f"Tuple is: {t1}")
print(f"Total of all elements in the tuple is: {sum(t1)}")
print("\n")

