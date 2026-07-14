"""
Assignment 4
Task 1 :- Read a File and Handle Errors

Description:-

* Opens and reads a text file named sample.txt.
* Prints its content line by line.
* Handles errors gracefully if the file does not exist.
"""
file_name = "sample.txt"

# Create file and write data
try:
    with open(file_name, "x") as file:
        file.write(
"""This is a sample text file.
It contains multiple lines."""
        )
except FileExistsError:
    print(f"The file '{file_name}' is already exists.")

# Read file and display content
try:
    with open(file_name, "r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error : The file '{file_name}' was not found.")
