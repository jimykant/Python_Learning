"""
Nested Lists in Python
----------------------------------------------------------
A nested list is a list that contains one or more lists
as its elements. It allows us to store data in multiple
levels (a list inside another list).

In this program, we will:
1. Create lists containing nested lists.
2. Find the length of the lists.
3. Access the nested list using indexing.
4. Retrieve the first and last elements of the nested list.
"""
print("Nested Lists in Python:-")
l1 = [5, 1.5, "Python", True, None, [1, 2, 3], 10]
print(f"List-1:- {l1}")
print(f"Length of the above list is:- {len(l1)}")
print(f"The Second-last element of the list is: '{l1[-2]}' and it is nested list")
print(f"The First element of the nested list is: {l1[-2][0]}")
print(f"The Last element of the nested list is: {l1[-2][-1]}")
print("\n")

l2 = [[1, 2], [3, 4],[5, 6, [0, 1]]]
print(f"List-2:- {l2}")
print(f"Length of the above list is:- {len(l2)}")
print(f"The Last element of the list is: '{l2[-1]}' and it is nested list")
print(f"The First element of the nested list is: {l2[-1][0]}")
print(f"The Last element of the nested list is: {l2[-1][-1]}")
