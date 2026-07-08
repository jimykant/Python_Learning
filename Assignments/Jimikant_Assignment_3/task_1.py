"""
Assignment 3
Task 1 :- Calculate Factorial Using a Function

Description:-

* Defines a function named factorial that takes a number as an argument
  and calculates its factorial using a loop or recursion.
* Returns the calculated factorial.
* Calls the function with a sample number and prints the output.
"""

def factorial(number):
    if number == 1:
        return 1
    else:
        result = number * factorial(number - 1)
        return result

def validation():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number <= 0:
                print("Please enter a positive number")
                continue
            else:
                return number
        except ValueError:
            print("Invalid Input!!! Please enter a numbers only")

if __name__ == "__main__":
    num = validation()
    print(f"Factorial of {num} is: {factorial(num)}")
