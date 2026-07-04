"""
Assignment 1'
Task 2 :- Personalized greeting using User-Inputs (Hello, John Doe! Welcome to the Python program.)
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name + "!" # OR
# full_name = f"{first_name} {last_name}"
print("Hello,", full_name, "Welcome to the Python program.")
