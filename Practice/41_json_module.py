"""
==========================================================
JSON MODULE IN PYTHON
==========================================================
Description:
    - JSON stands for JavaScript Object Notation.
    - JSON is a lightweight format used to store and exchange data.
    - It is commonly used in APIs, web applications, databases,
      configuration files, and data transfer between systems.
Why Use JSON?
    - Human-readable format.
    - Easy to share data between different programming languages.
    - Supported by most modern applications and web services.
Common Functions:
    - json.dump()  -> Write Python object to JSON file.
    - json.load()  -> Read JSON file into Python object.
    - json.dumps() -> Convert Python object to JSON string.
    - json.loads() -> Convert JSON string to Python object.
"""
import json

students = {
    "student1": {
        "roll": 101,
        "name": "John",
        "percent": 98.5,
        "sports": True
    },
    "student2": {
        "roll": 102,
        "name": "Carol",
        "percent": 92.5,
        "sports": False
    },
    "student3": {
        "roll": 103,
        "name": "Alice",
        "percent": 81.5,
        "sports": True
    }
}

"""
----------------------------------------------------------
1. Create a Python Dictionary
----------------------------------------------------------
Description:
    - Creates a dictionary containing student data.
    - This dictionary will later be stored in a JSON file.
Syntax:
    - dictionary_name = {key: value}
"""
print("1. Create a Python Dictionary")
print(students)
print(f"Data Type : {type(students)}")
print("\n")

"""
----------------------------------------------------------
2. Write Data to JSON File Using dump()
----------------------------------------------------------
Description:
    - Stores Python dictionary data inside a JSON file.
    - indent=4 improves readability.
Syntax:
    - json.dump(data, file_handler)
    - json.dump(data, file_handler, indent=4)
"""
print("2. Write Data to JSON File Using dump()")
with open("42_student_data.json", "tx") as file_handler:
    json.dump(students, file_handler, indent=4)
print("Data Written Successfully")
print("\n")

"""
----------------------------------------------------------
3. Read JSON File Using load()
----------------------------------------------------------
Description:
    - Reads JSON file data.
    - Converts JSON data back into a Python dictionary.
Syntax:
    - data = json.load(file_handler)
"""
print("3. Read JSON File Using load()")
with open("42_student_data.json", "tr") as file_handler:
    data = json.load(file_handler)
print(data)
print(f"Data Type : {type(data)}")
print("\n")

"""
----------------------------------------------------------
4. Update Existing JSON File
----------------------------------------------------------
Description:
    - Reads existing JSON data.
    - Updates the data using dictionary update().
    - Writes the updated data back to the JSON file.
Syntax:
    - dictionary.update(new_data)
Note:
    - Existing keys are updated.
    - New keys are added.
"""
print("4. Update Existing JSON File")
try:
    with open("42_student_data.json", "tr") as file_handler:
        data = json.load(file_handler)
except FileNotFoundError:
    print("JSON File Not Found")
    print("Creating New JSON File")
    with open("42_student_data.json", "tw") as file_handler:
        json.dump(students, file_handler, indent=4)
else:
    data.update(students)
    with open("42_student_data.json", "tw") as file_handler:
        json.dump(data, file_handler, indent=4)
    print("JSON File Updated Successfully")
