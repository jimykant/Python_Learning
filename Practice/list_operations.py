"""
List :- We can store the collection of data in to single variable or data-type
"""
student = ["John", 20, 85.5]
print(student)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[0])
print(f"Last day of the week is: {days_of_week[-1]}")

# Length of the list :- The number of the Items/Elements in the list
print(f"There are {len(days_of_week)}days in a week")
print("\n")

# Operations on the list
print("# Let's see some Operations on the List :-")
# Slicing of the list
print("1. Slicing of the list")
l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(f"List is:- {l1}")
print(l1[1:6:1])
print(l1[1:8:20])
print("\n")

# Concatenation of list
print("2. Concatenation of list")
l1 = [1, 7, 2]
print(f"List-1 is:- {l1}")
l2 = [0, 5]
print(f"List-2 is:- {l2}")
print(l1 + l2)
print(l2 + l1)
print("\n")

# Repetition of list (*)
print("3. Repetition of list (*)")
print(f"List is:- {l2}")
print(l2 * 3)
print("\n")

# Smallest number in the list
print("4. Smallest number in the list")
numbers = [10, 4, -1, 20, 5.5, 7, 1]
print("Numbers list:-", numbers)
print(f"Smallest number: {min(numbers)}")
print("\n")

# Biggest number in the list
print("5. Biggest number in the list")
print("Numbers list:-", numbers)
print(f"Biggest number: {max(numbers)}")
print("\n")

# sum() - It gives the total of all numbers in the list
print("6. sum() - It gives the total of all numbers in the list")
numbers = [10, 4, -1, 20, 5.5, 7, 1]
print(f"Number List:- {numbers}")
print(f"Total of numbers: {sum(numbers)}")
print("\n")

# in - it gives you "True" if the item is present in the list (Checking the Membership)
print("7. in - it gives you \"True\" if the item is present in the list (Checking the Membership)")
language = ["Python", "Java", "C++"]
print(f"Language List:- {language}")
print("Python" in language)
print("JavaScript" in language)
print("\n")

# not in - it gives you "True" if the item is NOT present in the list (Checking the Membership)
print("8. in - it gives you \"True\" if the item is NOT present in the list (Checking the Membership)")
print(f"Language List:- {language}")
print("Python" not in language)
print("JavaScript" not in language)
