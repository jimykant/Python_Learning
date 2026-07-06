"""
==========================================================
Lambda Functions
==========================================================
Description:
    - A Lambda Function is an 'anonymous' function.
    - 'Anonymous' means the function does not have a 'name' defined using 'def'.
    - Lambda functions are generally used for small, simple operations.
    - They can take any number of arguments but contain only 'one expression'.
    - The expression result is returned automatically.
"""
"""
----------------------------------------------------------
1. Lambda Function with One Argument
----------------------------------------------------------
Description:
    - Create a lambda function that adds 1 to a number.
    - The lambda function is assigned to a variable.
Syntax:
    - variable_name = lambda argument : expression
Note:
    - The 'expression' is automatically returned.
    - No 'return' keyword is required.
"""
print("1. Lambda Function with One Argument")
fun = lambda a : a + 1  # Anonymous function stored in variable 'fun'
result = fun(4)  # Call the lambda function
print(f"Result : {result}")
print("\n")

"""
----------------------------------------------------------
2. Lambda Function with Multiple Arguments
----------------------------------------------------------
Description:
    - Lambda functions can accept multiple arguments.
    - The expression can use all provided arguments.
Syntax:
    - variable_name = lambda arg1, arg2 : expression
"""
print("2. Lambda Function with Multiple Arguments")
add_fun = lambda a, b : a + b  # Add two numbers
result = add_fun(3, 3)  # Call the lambda function
print(f"Result : {result}")
print("\n")

"""
==========================================================
Lambda Functions, filter() and map()
==========================================================
"""
print("# Lambda Functions, filter() and map()")
"""
----------------------------------------------------------
1. filter() Function with Lambda
----------------------------------------------------------
Description:
    - filter() selects elements from a sequence.
    - Only elements for which the function returns 'True' are kept.
    - The result is a 'filter-object'. need to convert it to 'list'.
Syntax:
    - filter(function_name, sequence)
    - filter(lambda arguments : condition, sequence)
Note:
    - Convert the 'filter-object' to a 'list' using list().
"""
print("1. filter() Function with Lambda")
seq = [1, 2, 3, 4]
print(f"Sequence : {seq}")
odd_num = lambda x: True if x % 2 != 0 else False  # Keep only odd numbers
filtered_output = filter(odd_num, seq)
# OR filtered_output = filter(lambda x: True if x % 2 != 0 else False, seq)
print(f"Filter Object : {filtered_output}")
print(f"Odd Numbers : {list(filtered_output)}")
print("\n")

"""
----------------------------------------------------------
2. map() Function with Lambda
----------------------------------------------------------
Description:
    - map() applies an expression to every element of a sequence.
    - The result contains transformed values.
    - The result is a 'map-object'. need to convert it to 'list'.
Syntax:
    - map(function_name, sequence)
    - map(lambda arguments : expression, sequence)
Note:
    - Convert the 'map-object' to a 'list' using list().
"""
print("2. map() Function with Lambda")
seq = [1, 2, 3, 4]
print(f"Sequence : {seq}")
mapped_output = map(lambda x: x ** 2, seq)  # Square each element
print(f"Map Object : {mapped_output}")
print(f"Squared Values : {list(mapped_output)}")
