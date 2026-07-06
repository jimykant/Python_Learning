"""
==========================================================
Local and Global Variables
==========================================================
Description:
    - Variables created inside a function are called Local Variables.
    - Variables created outside a function are called Global Variables.
    - Local variables can be accessed only inside their function.
    - Global variables can be accessed throughout the program.
"""
"""
----------------------------------------------------------
1. Local Variable
----------------------------------------------------------
Description:
    - A local variable is created inside a function.
    - It exists only while the function is executing.
    - It cannot be accessed outside the function.
Syntax:
    - def function_name():
          variable_name = value
"""
print("1. Local Variable")
def greeting():
    name = "Jimi"  # Local variable
    print(f"Inside Function : {name}")
greeting()  # function call
# print(f"Outside Function : {name}")  # Error: name is not accessible outside the function
print("\n")

"""
----------------------------------------------------------
2. Global Variable
----------------------------------------------------------
Description:
    - A global variable is created outside a function.
    - It can be accessed inside and outside functions.
Syntax:
    - variable_name = value
"""
print("2. Global Variable")
country = "Australia"  # Global variable
def show_country():
    print(f"Inside Function : {country}")
show_country()  # function call
print(f"Outside Function : {country}")  # variable print
print("\n")

"""
----------------------------------------------------------
3. Local Variable and Global Variable with Same Name
----------------------------------------------------------
Description:
    - A local variable takes priority over a global variable
      inside the function.
    - Outside the function, the global variable is used.
"""
print("3. Local Variable and Global Variable with Same Name")
name = "Global Jimi"  # Global variable
def display_name():
    name = "Local Jimi"  # Local variable (takes priority over global-variable)
    print(f"Inside Function : {name}")
display_name()  # function call
print(f"Outside Function : {name}")
print("\n")

"""
----------------------------------------------------------
4. Modifying a Global Variable Using global Keyword
----------------------------------------------------------
Description:
    - By default, a function cannot modify a global variable.
    - Use the 'global' keyword to modify the global variable.
Syntax:
    - global variable_name
"""
print("4. Modifying a Global Variable Using global Keyword")
count = 10  # Global variable
def update_count():
    global count  # Refer to the global variable
    count += 5
    print(f"Inside Function : {count}")
update_count()  # function call
print(f"Outside Function : {count}")
print("\n")

"""
----------------------------------------------------------
5. Accessing Global Variable Without global Keyword
----------------------------------------------------------
Description:
    - A global variable can be read inside a function
      without using the global keyword.
    - global is required only when modifying the variable.
"""
print("5. Accessing Global Variable Without global Keyword")
message = "Welcome to Python"  # Global variable
def show_message():
    print(f"Inside Function : {message}")
show_message()
print(f"Outside Function : {message}")
