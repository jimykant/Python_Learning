"""
Simple Interest (SI)

Formula:-
    Simple Interest = (P * R * T) / 100

P = Principal Amount
R = Rate of Interest
T = Time (in years)
"""

p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the Rate of Interest: "))
t = float(input("Enter the Time (in years): "))

si = (p * r * t) / 100
print("Simple Interest is:", round(si, 2))
