"""
==========================================================
Printing Variables and Calculating Marks
==========================================================
Description:
    - Learn how to print variables, use f-strings,
      and calculate total, average, and percentage.
"""

"""
----------------------------------------------------------
1. Printing Variables
----------------------------------------------------------
Description:
    - Prints variables using comma-separated arguments.
Syntax:
    - print(variable1, variable2, ...)
"""
name = "John"
age = 20
language = "Python"
hours = 3
print("1. Printing Variables")
# John is 20 years old.
print(name, "is", age, "years old.")
# John studies Python.
print(name, "is", age, "years old. He studies", language, hours, "hours a day.")
print("\n")

"""
----------------------------------------------------------
2. Using f-Strings
----------------------------------------------------------
Description:
    - Prints formatted text using f-strings.
Syntax:
    - print(f"{variable}")
"""
print("2. Using f-Strings")
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")
print("\n")

"""
----------------------------------------------------------
3. Total Marks
----------------------------------------------------------
Description:
    - Calculates and prints the total marks.
Syntax:
    - variable1 + variable2 + variable3
"""
sub1 = 78
sub2 = 87
sub3 = 83
print("3. Total Marks")
print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")
print(name, "scored", sub1 + sub2 + sub3, "marks in total.")
print("\n")

"""
----------------------------------------------------------
4. Average Marks
----------------------------------------------------------
Description:
    - Calculates the average marks.
Syntax:
    - average = total / number_of_subjects
"""
print("4. Average Marks")
avg = (sub1 + sub2 + sub3) / 3
print(f"{name} got {round(avg, 1)} average marks.")
print("\n")

"""
----------------------------------------------------------
5. Percentage
----------------------------------------------------------
Description:
    - Calculates the percentage of marks.
Syntax:
    - percentage = (obtained_marks / total_marks) * 100
"""
print("5. Percentage")
obtained_marks = sub1 + sub2 + sub3
total_marks = 300
percent = (obtained_marks / total_marks) * 100
print(f"{name} got {round(percent, 2)}%")
