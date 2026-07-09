"""
==========================================================
File Handling in Python
==========================================================
Description:
    - File handling allows us to create, read, write, and update files.
    - Python provides the open() function to perform file operations.

Modes:
    - r  : Read
    - x  : Create
    - w  : Write (Overwrite)
    - a  : Append
    - t  : Text File
    - b  : Binary File
"""

"""
----------------------------------------------------------
1. Create a File Using x Mode
----------------------------------------------------------
Description:
    - Creates a new file.
    - Raises FileExistsError if the file already exists.
Syntax:
    - open(file_name, "x")
"""
print("1. Create a File Using x Mode")

file_handler = open("40_content.txt", "tx")

# Write content into the file
file_handler.write(
"""This is a test file.
We are learning File Handling in Python.
Modes to open a file are:- Read(r), Create(x), Over-write(w), Append(a), Text-file(t), Binary-file(b).
""")
# Close the file after writing
file_handler.close()
print("File created successfully.")
print("\n")

"""
----------------------------------------------------------
2. Read Entire File Using read()
----------------------------------------------------------
Description:
    - Reads the complete content of a file.
Syntax:
    - file.read()
"""
print("2. Read Entire File Using read()")

file_handler = open("40_content.txt", "tr")
print(f"File Handler : {file_handler}")

content = file_handler.read()
# Close the file
file_handler.close()

print("Complete File Content:")
print(content)
print(f"Data Type : {type(content)}")
print("\n")

"""
----------------------------------------------------------
3. Read First N Characters Using read(size)
----------------------------------------------------------
Description:
    - Reads a specific number of characters.
Syntax:
    - file.read(number_of_characters)
"""
print("3. Read First N Characters Using read(size)")

file_handler = open("40_content.txt", "tr")
content = file_handler.read(10)
# Close the file
file_handler.close()

print(f"First 10 Characters : {content}")
print("\n")

"""
----------------------------------------------------------
4. Read First Line Using readline()
----------------------------------------------------------
Description:
    - Reads one line at a time.
Syntax:
    - file.readline()
"""
print("4. Read First Line Using readline()")

file_handler = open("40_content.txt", "tr")
content = file_handler.readline()
# Close the file
file_handler.close()

print(f"First Line : {content}")
print("\n")

"""
----------------------------------------------------------
5. Read All Lines Using readlines()
----------------------------------------------------------
Description:
    - Reads all lines and stores them in a list.
    - Each list element represents one line.
Syntax:
    - file.readlines()
"""
print("5. Read All Lines Using readlines()")

file_handler = open("40_content.txt", "tr")
content = file_handler.readlines()
# Close the file
file_handler.close()

print("All Lines:")
print(content)

print("\nLines Using for Loop:")
for line in content:
    print(line, end="")
    # print(line.rstrip("\n"))
print("\n")

"""
----------------------------------------------------------
6. Close a File Using close()
----------------------------------------------------------
Description:
    - Releases system resources used by the file.
    - After closing, file operations cannot be performed.
Syntax:
    - file.close()
"""
print("6. Close a File Using close()")

file_handler = open("40_content.txt", "tr")
print(f"Before Closing : {file_handler}")
# Close the file
file_handler.close()

print(f"After Closing : {file_handler}")
print("\n")

"""
----------------------------------------------------------
7. Overwrite File Using w Mode
----------------------------------------------------------
Description:
    - Opens a file for writing.
    - Deletes existing content.
    - Creates the file if it does not exist.
Syntax:
    - open(file_name, "w")
"""
print("7. Overwrite File Using w Mode")

file_handler = open("40_content.txt", "tw")

file_handler.write(
"""This file is over-written using 'w' mode in Python.
Have a nice day!!!
""")
# Close the file
file_handler.close()
print("File overwritten successfully.")
print("\n")

"""
----------------------------------------------------------
8. Get Current File Pointer Position Using tell()
----------------------------------------------------------
Description:
    - Returns the current position of the file pointer.
    - Position is returned as an integer.
    - Useful for tracking where reading or writing is occurring.
Syntax:
    - file.tell()
"""
print("8. Get Current File Pointer Position Using tell()")

file_handler = open("40_content.txt", "tr")
print(f"Initial Position : {file_handler.tell()}")

content = file_handler.read(10)
print(f"Content Read : {content}")
print(f"Current Position : {file_handler.tell()}")
# Close the file
file_handler.close()
print("\n")

"""
----------------------------------------------------------
9. Move File Pointer Using seek()
----------------------------------------------------------
Description:
    - Moves the file pointer to a specified position.
    - seek(0) moves the pointer to the beginning of the file.
Syntax:
    - file.seek(position)
"""
print("9. Move File Pointer Using seek()")

file_handler = open("40_content.txt", "tr")
content = file_handler.read(10)

print(f"First Read : {content}")
print(f"Position After Read : {file_handler.tell()}")

file_handler.seek(0)
print(f"Position After seek(0) : {file_handler.tell()}")

content = file_handler.read(10)
print(f"Read Again : {content}")
# Close the file
file_handler.close()
print("\n")

"""
----------------------------------------------------------
10. Append Content to File Using 'a' Mode
----------------------------------------------------------
Description:
    - Appends new content at the end of an existing file.
    - 'a' mode adds content at the end of the file.
    - If the file does not exist, it creates a new file.
Syntax:
    - file_handler = open(file_name, "ta")
    - file_handler.write(content)
"""
print("10. Append Content to File Using 'a' Mode")
file_handler = open("40_content.txt", "ta")
file_handler.write(
"""This content has been writen using 'a' mode.
'a' mode is used to add new content at the end of the file.
also 'a' mode creates new file if it does not exist.
Good bye!!!
""")
# Close the file
file_handler.close()
print("Content Appended Successfully")
