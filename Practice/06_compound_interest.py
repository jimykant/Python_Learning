"""
Compound Interest (CI)

Formula:-
    Amount = P * (1 + R / 100) ** T
    OR
    Amount = P * pow((1 + R / 100), T)

    Compound Interest = Amount - P
"""

p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the Rate of Interest: "))
t = float(input("Enter the Time (in years): "))

# Method 1: Using pow() Function
# amount = p * pow((1 + r / 100), t)

# Method 2: Using Exponent Operator (**)
amount = p * (1 + r / 100) ** t
print("Total Amount after interest is:", round(amount, 2))

ci = amount - p
print("Compound Interest is:", round(ci, 2))