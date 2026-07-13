"""
==========================================================
EXCEPTION HANDLING IN PYTHON
==========================================================
Description:
    - Exception handling prevents a program from crashing.
    - It allows us to handle errors gracefully.
    - Python provides try, except, else, and finally blocks.
Common Exceptions:
    - ValueError
    - ZeroDivisionError
    - FileNotFoundError
    - IndexError
    - KeyError
"""
"""
----------------------------------------------------------
1. Handle Multiple Exceptions Using try-except
----------------------------------------------------------
Description:
    - Handles different types of errors.
    - Program continues running even if an error occurs.
Syntax:
    - try:
          risky_code
      except ExceptionName:
          handling_code
Note:
    - Multiple except blocks can be used.
"""
print("1. Handle Multiple Exceptions Using try-except")
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))
    result = num1 / num2
    print(f"Result : {result}")
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Input should contain only numbers")
print("\n")

"""
----------------------------------------------------------
2. Handle FileNotFoundError
----------------------------------------------------------
Description:
    - Handles errors while opening files.
    - Prevents program crash if file does not exist.
Syntax:
    - try:
          open(file)
      except FileNotFoundError:
          handling_code
"""
print("2. Handle FileNotFoundError")
try:
    with open("my_file.txt", "tr") as file_handler:
        data = file_handler.read()
    print(data)
except FileNotFoundError as file_error:
    print("The file you are trying to open does not exist")
    print(file_error)
print("\n")

"""
----------------------------------------------------------
3. Use else Block with try-except
----------------------------------------------------------
Description:
    - else executes only when no exception occurs.
    - Useful for code that should run after successful execution.
Syntax:
    - try:
          risky_code
      except Exception:
          handling_code
      else:
          success_code
Note:
    - else block is skipped if an exception occurs.
"""
print("3. Use else Block with try-except")
try:
    with open("40_content.txt", "tr") as file_handler:
        data = file_handler.read()
except FileNotFoundError as file_error:
    print("The file you are trying to open does not exist")
    print(file_error)
else:
    print("Else Block Executed")
    print("File Opened Successfully")
    print(data)
print("\n")

"""
----------------------------------------------------------
4. Use finally Block with try-except
----------------------------------------------------------
Description:
    - finally always executes.
    - Used for cleanup operations.
    - Commonly used to close files, database connections,
      network connections, etc.
Syntax:
    - try:
          risky_code
      except Exception:
          handling_code
      finally:
          cleanup_code
Note:
    - finally runs whether an exception occurs or not.
"""
print("4. Use finally Block with try-except")
file_handler = None
try:
    file_handler = open("my_file.txt", "tr")
    data = file_handler.read()
    print(data)
except FileNotFoundError as file_error:
    print("The file you are trying to open does not exist")
    print(file_error)
finally:
    print("Finally Block Executed")
    if file_handler:
        file_handler.close()
        print("File Closed Successfully")
    else:
        print("No File Available to Close")
print("\n")

"""
----------------------------------------------------------
5. Complete Flow of try-except-else-finally
----------------------------------------------------------
Description:
    - Demonstrates the execution flow of all blocks.
Execution Order:
    - try
    - except (if exception occurs)
    - else (if no exception occurs)
    - finally (always executes)
"""
print("5. Complete Flow of try-except-else-finally")
try:
    num = int(input("Enter a number : "))
except ValueError:
    print("Only numbers are allowed")
else:
    print(f"You Entered : {num}")
finally:
    print("Program Finished")
print("\n")

"""
----------------------------------------------------------
6. Raise Exception Using raise
----------------------------------------------------------
Description:
    - The 'raise' keyword is used to manually generate an 'exception'.
    - Useful when input data does not meet program requirements.
    - Program stops immediately when an exception is raised.
    - Custom error messages can be provided.
Syntax:
    - raise ExceptionName("Error Message")
"""
print("6. Raise Exception Using raise")
age = float(input("Enter your age : "))
if age <= 0:
    raise ValueError("Age cannot be negative or zero!")
    # raise Exception("Age cannot be negative or zero!")  # You can write it generally
else:
    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("You cannot vote!")
