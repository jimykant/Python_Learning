"""
----------------------------------------------------------
1. continue Statement
----------------------------------------------------------
Description:
    - continue skips the current iteration of the loop.
    - The remaining code inside the loop is not executed for that iteration.
    - The loop then moves to the next iteration.
Syntax:
    - if condition:
          continue
"""
print("1. continue Statement")
for num in range(10):
    if num % 3 == 0:
        continue  # it skips this current iteration and move to next one
    print(num)  # this 'num' is not print if num % 3 == 0
"""
Note:
    - Numbers divisible by 3 are skipped.
    - The loop continues with the next number.
"""
print("\n")

"""
----------------------------------------------------------
2. break Statement
----------------------------------------------------------
Description:
    - break immediately terminates the loop.
    - The loop stops as soon as the break statement is executed.
    - No further iterations are performed.
Syntax:
    - if condition:
          break
"""
print("2. break Statement")

for num in range(1, 10):
    if num % 3 == 0:
        break  # it will break the entire loop
    print(num)  # if it encounters the first number divisible by 3 then it will exit the loop
"""
Note:
    - The loop stops when it encounters the first number divisible by 3.
    - Remaining iterations are not executed.
"""
