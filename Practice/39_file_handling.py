"""
==========================================================
FILE HANDLING IN PYTHON
==========================================================
Description:
    - File handling allows us to create, read, write, and update files.
File Modes:
    - r -> Read
    - x -> Create
    - w -> Write (Overwrite)
    - a -> Append
    - t -> Text File
    - b -> Binary File
"""
import os
from pathlib import Path

FILE_NAME = "40_content.txt"

"""
----------------------------------------------------------
1. Create a File Using 'x' Mode
----------------------------------------------------------
Description:
    - Creates a new file.
Syntax:
    - open(file_name, "tx")
Note:
    - Raises FileExistsError if file already exists.
"""
print("1. Create a File Using 'x' Mode")
if os.path.exists(FILE_NAME):
    print(f"File Exists : {FILE_NAME}")
else:
    print("File does not exist. Creating it...")
    file_handler = open(FILE_NAME, "tx")
    file_handler.write("""This is a test file.
We are learning File Handling in Python.
Modes to open a file are:
Read(r), Create(x), Overwrite(w), Append(a),
Text File(t), Binary File(b).
""")
    file_handler.close()
    print("File Created Successfully")
print("\n")

"""
----------------------------------------------------------
2. Read Entire File Using read()
----------------------------------------------------------
Description:
    - Reads complete file content.
Syntax:
    - file.read()
"""
print("2. Read Entire File Using read()")
file_handler = open(FILE_NAME, "tr")
print(f"File Handler : {file_handler}")
content = file_handler.read()
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
    - Reads specified number of characters.
Syntax:
    - file.read(size)
"""
print("3. Read First N Characters Using read(size)")
file_handler = open(FILE_NAME, "tr")
content = file_handler.read(10)
file_handler.close()
print(f"First 10 Characters : {content}")
print("\n")

"""
----------------------------------------------------------
4. Read First Line Using readline()
----------------------------------------------------------
Description:
    - Reads one line from file.
Syntax:
    - file.readline()
"""
print("4. Read First Line Using readline()")
file_handler = open(FILE_NAME, "tr")
content = file_handler.readline()
file_handler.close()
print(f"First Line : {content}")
print("\n")

"""
----------------------------------------------------------
5. Read All Lines Using readlines()
----------------------------------------------------------
Description:
    - Reads all lines and returns a list.
Syntax:
    - file.readlines()
"""
print("5. Read All Lines Using readlines()")
file_handler = open(FILE_NAME, "tr")
content = file_handler.readlines()
file_handler.close()
print("All Lines:")
print(content)
print("\nLines Using for Loop:")
for line in content:
    print(line, end="")
print("\n")

"""
----------------------------------------------------------
6. Close a File Using close()
----------------------------------------------------------
Description:
    - Closes an opened file.
Syntax:
    - file.close()
"""
print("6. Close a File Using close()")
file_handler = open(FILE_NAME, "tr")
print(f"Before Closing : {file_handler}")
file_handler.close()
print(f"After Closing  : {file_handler}")
print("\n")

"""
----------------------------------------------------------
7. Overwrite File Using 'w' Mode
----------------------------------------------------------
Description:
    - Replaces existing file content.
Syntax:
    - open(file_name, "tw")
Note:
    - Creates file if it does not exist.
"""
print("7. Overwrite File Using 'w' Mode")
file_handler = open(FILE_NAME, "tw")
file_handler.write(
"""This file is overwritten using 'w' mode in Python.
Have a nice day!!!
""")
file_handler.close()
print("File Overwritten Successfully")
print("\n")

"""
----------------------------------------------------------
8. Get Current File Pointer Position Using tell()
----------------------------------------------------------
Description:
    - Returns current file pointer position.
Syntax:
    - file.tell()
"""
print("8. Get Current File Pointer Position Using tell()")
file_handler = open(FILE_NAME, "tr")
print(f"Initial Position : {file_handler.tell()}")
content = file_handler.read(10)
print(f"Content Read     : {content}")
print(f"Current Position : {file_handler.tell()}")
file_handler.close()
print("\n")

"""
----------------------------------------------------------
9. Move File Pointer Using seek()
----------------------------------------------------------
Description:
    - Moves file pointer to a specified position.
Syntax:
    - file.seek(position)
Note:
    - seek(0) moves pointer to beginning.
"""
print("9. Move File Pointer Using seek()")
file_handler = open(FILE_NAME, "tr")
content = file_handler.read(10)
print(f"First Read             : {content}")
print(f"Position After Read    : {file_handler.tell()}")
file_handler.seek(0)
print(f"Position After seek(0) : {file_handler.tell()}")
content = file_handler.read(10)
print(f"Read Again             : {content}")
file_handler.close()
print("\n")

"""
----------------------------------------------------------
10. Append Content Using 'a' Mode
----------------------------------------------------------
Description:
    - Adds new content at the end of file.
Syntax:
    - open(file_name, "ta")
Note:
    - Creates file if it does not exist.
"""
print("10. Append Content Using 'a' Mode")
file_handler = open(FILE_NAME, "ta")
file_handler.write(
"""This content has been written using 'a' mode.
'a' mode is used to add content at the end of the file.
It also creates a new file if it does not exist.
Good Bye!!!
""")
file_handler.close()
print("Content Appended Successfully")
print("\n")

"""
----------------------------------------------------------
11. Read File Using with Statement
----------------------------------------------------------
Description:
    - Automatically closes file after use.
Syntax:
    - with open(file_name, mode) as file:
"""
print("11. Read File Using with Statement")
with open(FILE_NAME, "tr") as file_handler:
    content = file_handler.read(20)
print(f"Content : {content}")
print("\n")

"""
----------------------------------------------------------
12. Check File Existence Using os.path.exists()
----------------------------------------------------------
Description:
    - Checks whether a file exists.
Syntax:
    - os.path.exists(path)
"""
print("12. Check File Using os.path.exists()")
if os.path.exists(FILE_NAME):
    print(f"File Exists using os : {FILE_NAME}")
else:
    print("File Not Exists")
print("\n")

"""
----------------------------------------------------------
13. Check File Existence Using pathlib.Path.exists()
----------------------------------------------------------
Description:
    - Checks file existence using pathlib.
Syntax:
    - Path(path).exists()
"""
print("13. Check File Using pathlib.Path.exists()")
file_path = Path("/home/jarvis/Python_Learning/Practice/40_content.txt")
if file_path.exists():
    print(f"File Exists using pathlib : {file_path}")
else:
    print("File Not Exists")
