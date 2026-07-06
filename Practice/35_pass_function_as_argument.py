# In python, we can pass a function as argument of another function

def add_1(num):
    result = num + 1
    return result
# print(add_1(5))

def square(num):
    result = num ** 2
    return result
# print(square(4))

num = int(input("Enter a number: "))
result = square(add_1(num)) # first add(1) to the number then do square of it
print(f"Add +1 to '{num}' and then do square of {add_1(num)}, gives: {result}")
