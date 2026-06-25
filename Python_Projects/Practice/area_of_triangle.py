"""
Formula:-
    Area = (B * H) / 2
    OR
    Area = (B * H) / 2 OR 0.5 * (B * H)

B = Base
H = Height
"""

b = float(input("Enter the Base: "))
h = float(input("Enter the Height: "))

area = (b * h) / 2
print("The Area of this Triangle is:", round(area, 2))
