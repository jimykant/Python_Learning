"""
Assignment 3
Task 2 :- Write and Append Data to a File

Description:-

* Takes user input and writes it to a file named output.txt.
* Appends additional data to the same file.
* Reads and displays the final content of the file.
"""

# First user input
text = input("Enter text to write to the file: ")
with open("output.txt", "tw") as file:
     file.write(text + "\n")
print("Data successfully written to output.txt.")

# Second user input
add_text = input("\nEnter additional text to append: ")
with open("output.txt", "ta") as file:
    file.write(add_text + "\n")
print("Data successfully appended.")

# Read the final content
print("\nFinal content of output.txt:")
with open("output.txt", "tr") as file:
    content = file.read()
print(content)