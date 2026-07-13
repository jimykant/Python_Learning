"""
==========================================================
PICKLE MODULE IN PYTHON
==========================================================
Description:
    - Pickle is a built-in Python module used to store Python
      objects in binary files.
    - It converts Python objects into a byte stream.
    - This process is called Serialization.
    - The stored byte stream can later be converted back into
      Python objects.
    - This process is called Deserialization.
Why Use Pickle?
    - Stores Python objects directly.
    - Supports dictionaries, lists, tuples, sets, classes, etc.
    - Faster than JSON for Python-to-Python communication.
    - Useful for saving application data and ML models.
Common Functions:
    - pickle.dump() -> Store object in binary file.
    - pickle.load() -> Read object from binary file.
Important:
    - Pickle files are not human-readable.
    - Use Pickle only with trusted files.
"""
import pickle

students = {
    "student1": {
        "roll": 101,
        "name": "John",
        "percent": 98.5
    },
    "student2": {
        "roll": 102,
        "name": "Carol",
        "percent": 91.5
    },
    "student3": {
        "roll": 103,
        "name": "Alice",
        "percent": 71.0
    }
}

"""
----------------------------------------------------------
1. Create a Python Dictionary
----------------------------------------------------------
Description:
    - Creates a dictionary containing student information.
    - This data will be stored inside a binary file.
Syntax:
    - dictionary_name = {key: value}
"""
print("1. Create a Python Dictionary")
print(students)
print(f"Data Type : {type(students)}")
print("\n")

"""
----------------------------------------------------------
2. Serialization Using pickle.dump()
----------------------------------------------------------
Description:
    - Serialization converts Python objects into byte streams.
    - The byte stream is stored inside a binary file.
    - Binary files use 'b' mode.
    - Each pickle.dump() stores one Python object.
Syntax:
    - pickle.dump(object, file_handler)
Note:
    - Here we store each student's dictionary separately.
    - Therefore a loop is required.
"""
print("2. Serialization Using pickle.dump()")
with open("45_students_data.bin", "bx") as file_handler:
    for student in students:
        pickle.dump(students[student], file_handler)
print("Data Serialized Successfully")
print("\n")

"""
----------------------------------------------------------
3. Deserialization Using pickle.load()
----------------------------------------------------------
Description:
    - Deserialization converts byte streams back into
      Python objects.
    - Objects must be loaded in the same order they
      were stored.
Syntax:
    - pickle.load(file_handler)
Note:
    - pickle.load() reads only one object at a time.
    - EOFError occurs when no more objects remain.
"""
print("3. Deserialization Using pickle.load()")
with open("45_students_data.bin", "br") as file_handler:
    while True:
        try:
            data = pickle.load(file_handler)
            print(data)
            print(f"Data Type : {type(data)}")
        except EOFError:
            print("End Of File Reached")
            break
print("\n")

"""
----------------------------------------------------------
4. Find Students Scoring 90% or More
----------------------------------------------------------
Description:
    - Reads student records from the binary file.
    - Creates a list of students whose percentage
      is 90 or above.
Syntax:
    - list.append(value)
Note:
    - Since objects were stored separately,
      they must be loaded one by one.
"""
print("4. Find Students Scoring 90% or More")
student_list_90 = []
with open("45_students_data.bin", "br") as file_handler:
    while True:
        try:
            data = pickle.load(file_handler)
            if data["percent"] >= 90:
                student_list_90.append(data["name"])
        except EOFError:
            break
print(f"Students Who Secured 90% Or More : {student_list_90}")
