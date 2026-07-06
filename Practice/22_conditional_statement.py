"""
==========================================================
Conditional Statements in Python
==========================================================
Description:
    - Conditional statements are used to make decisions in a program.
    - A condition is evaluated as either True or False.
    - If the condition is True, the corresponding block of code is executed.
    Comparison Operators:
        ==   Equal To
        !=   Not Equal To
        >    Greater Than
        <    Less Than
        >=   Greater Than or Equal To
        <=   Less Than or Equal To
"""

"""
----------------------------------------------------------
1. if Statement
----------------------------------------------------------
Description:
    - Executes a block of code only when the condition is True.
    - Python uses indentation (spaces) to create blocks.
Syntax:
    - if condition:
          statement1
          statement2
"""
print("1. if Statement")
age = int(input("What is your age? : "))
if age >= 18:
    print("Congrats! You are an adult. You can now cast your vote.")
print("Thank you for your time!")
print("\n")

"""
----------------------------------------------------------
2. if-else Statement
----------------------------------------------------------
Description:
    - Executes one block when the condition is True.
    - Executes another block when the condition is False.
Syntax:
    - if condition:
          statement1
      else:
          statement2
"""
print("2. if-else Statement")
age = int(input("What is your age? : "))
if age >= 18:
    print("Congrats! You are an adult. You can now cast your vote.")
else:
    print("Few more years before you can vote.")
print("Thank you for your time!")
print("\n")

"""
----------------------------------------------------------
3. Checking Odd or Even Number
----------------------------------------------------------
Description:
    - A number is even if it is divisible by 2.
    - A number is odd if it is not divisible by 2.
    - The modulus operator (%) returns the remainder.
Syntax:
    - number % 2 == 0
"""
print("3. Checking Odd or Even Number")
num = int(input("Enter an integer : "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print("\n")

"""
----------------------------------------------------------
4. if-elif-else Statement
----------------------------------------------------------
Description:
    - Used when multiple conditions need to be checked.
    - Python evaluates conditions from top to bottom.
    - The first True condition is executed.
    - If none of the conditions are True, the else block is executed.
Syntax:
    - if condition1:
          statement1
      elif condition2:
          statement2
      elif condition3:
          statement3
      else:
          statementN
"""
print("4. if-elif-else Statement")
"""
Grade Criteria:
    >= 90         : Grade A
    80 to 89.99   : Grade B
    70 to 79.99   : Grade C
    60 to 69.99   : Grade D
    < 60          : Grade F
"""
marks = float(input("Enter your marks : "))
if marks >= 90:
    print("Grade is A")
elif 80 <= marks < 90:
    print("Grade is B")
elif 70 <= marks < 80:
    print("Grade is C")
elif 60 <= marks < 70:
    print("Grade is D")
else:
    print("Grade is F")
print("\n")

"""
----------------------------------------------------------
5. Nested if-elif-else Statement
----------------------------------------------------------
Description:
    - A nested if-elif-else statement is an if-elif-else statement inside another if block.
    - The outer condition is checked first.
    - If the outer condition is True, the inner conditions are evaluated.
    - Useful when one decision depends on another decision.
Syntax:
    - if condition1:
          if condition2:
              statement1
          elif:
              statement2
          else:
              statement3
      else:
          statement4
"""
print("5. Nested if-elif-else Statement")

"""
Grade Criteria:
    >= 90         : Grade A
    80 to 89.99   : Grade B
    70 to 79.99   : Grade C
    60 to 69.99   : Grade D
    < 60          : Fail
"""

marks = float(input("Enter your marks : "))

if marks >= 60:
    print("Congrats, you have passed the exam!")
    if marks >= 90:
        print("Your grade is A")
    elif 80 <= marks < 90:
        print("Your grade is B")
    elif 70 <= marks < 80:
        print("Your grade is C")
    else:
        print("Your grade is D")
else:
    print("You have failed, study hard next time")
print("\n")

"""
----------------------------------------------------------
6. Using Ternary Operator
----------------------------------------------------------
Description:
    - Performs the same operation as if-else in a single line.
    - The True expression is executed when the condition is True.
    - The False expression is executed when the condition is False.
Syntax:
    - true_expression if condition else false_expression
"""
print("2. Using Ternary Operator")
num = int(input("Enter a number : "))
result = "Even" if num % 2 == 0 else "Odd"
# print("Even") if num % 2 == 0 else print("Odd")
# print("Even" if num % 2 == 0 else "Odd")
print(result)
