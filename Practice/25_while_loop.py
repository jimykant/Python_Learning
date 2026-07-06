"""
==========================================================
While Loop in Python
==========================================================
Description:
    - A while loop executes a block of code as long as the condition remains True.
    - The condition is checked before every iteration.
    - When the condition becomes False, the loop stops.
"""

"""
----------------------------------------------------------
1. Basic while Loop
----------------------------------------------------------
Description:
    - Repeats a block of code while the condition is True.
    - The loop variable should be updated to avoid an infinite loop.
Syntax:
    - while condition:
          statement
"""
print("1. Basic while Loop")
num = 1
while num < 5:
    print(num)
    num += 1
print("\n")

"""
----------------------------------------------------------
2. Infinite while Loop with break
----------------------------------------------------------
Description:
    - while True creates an infinite loop.
    - break is used to terminate the loop when a condition is satisfied.
    - Useful when the number of iterations is unknown.
Syntax:
    - while True:
          statement
          if condition:
              break
"""
print("2. Infinite while Loop with break")
correct_password = "Python"
while True:
    user_password = input("Enter your password : ")
    if user_password == correct_password:
        print("Password is correct! Congrats.")
        break
    else:
        print("Password is incorrect. Try again.")
print("Logged in!")
print("\n")

"""
----------------------------------------------------------
3. Printing Even Numbers Using while Loop
----------------------------------------------------------
Description:
    - Prints even numbers within a specified range.
    - The loop variable is increased by 2 in each iteration.
Syntax:
    - while condition:
          statement
          variable += 2
"""
print("3. Printing Even Numbers from 10 to 20 Using while Loop")
num = 10
while num <= 20:
    print(num)
    num += 2
