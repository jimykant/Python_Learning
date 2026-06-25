"""
When all the length of the sides of the triangle is known - a, b, c
Formula:-
    Semi perimeter (s) = a + b + c / 2
    Area is = square root of (s * (s - a) * (s - b) * (s - c))
"""

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2
print("Semi-perimeter of triangle is: ", round(s, 2))

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # "0.5 is square root"
print("Area of triangle with given sides is: ", round(area, 2))
