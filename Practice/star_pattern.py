"""
----------------------------------------------------------
Star Pattern Using Nested for Loop
----------------------------------------------------------
Pattern :- 
* 
* * 
* * * 
* * * * 
* * * * *
Description:
    - A nested for loop can be used to print patterns.
    - The outer loop controls the number of rows.
    - The inner loop controls the number of stars printed in each row.
Syntax:
    - for row in range(start, end):
          for column in range(start, row + 1):
              statement
"""
print("12. Star Pattern Using Nested for Loop")

# Outer loop controls the rows (1 to 5)
for i in range(1, 6):

    # Inner loop prints stars in each row
    # Number of stars depends on the current value of i
    for j in range(1, i + 1):

        # Print star on the same line
        # end=" " prevents moving to the next line
        print("*", end=" ")

    # Move cursor to the next line after completing one row
    print()
