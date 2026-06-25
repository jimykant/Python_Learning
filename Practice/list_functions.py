"""
Functions of the List
"""

print("# Lets see some Functions of the list")
# append() Function - add only single item to the end of the list (any data-type)
# Syntax :- list.append(item)
print("1. append() - add only single items to the end of the list")
fruits = ["Mango", "Apple", "Orange"]
print(f"Fruit List is :- {fruits}")
fruits.append("Banana")
print(fruits)
print("\n")

# insert() Function - add only single item before the specific index of list item
# Syntax :- list.insert(index, item)
print("2. insert() - add only single item before the specific index of list item")
print(f"Fruit List is :- {fruits}")
fruits.insert(2, "Pineapple")
print(fruits)
print("\n")

# extend() Function - add multiple items/elements at the end of the list
# Syntax :- list.extedn(["item", "item"])
print("3. extend() - add multiple items/elements to the end of the list")
print(f"Fruit List is :- {fruits}")
fruits.extend(["Grapes", "Cherry"])
print(fruits)
print("\n")

# remove() Function - it remove certain item/element from the list
# Syntax :- list.remove(item_name from the list)
print("4. remove() - it removes only one item/element from the list")
print(f"Fruit List is :- {fruits}")
fruits.remove("Banana")
print(fruits)
print("\n")

# pop() Function - it removes the item/element from the list using index only
# OR if we don't give any index to it it will delete the last items of the list
# Syntax :- list.pop(index) OR list.pop()
print("""5. pop() - it removes the item/element from the list using index only
   OR if we don't give any index to it it will delete the last items of the list""")
print(f"Fruit List is :- {fruits}")
fruits.pop(3)
print(fruits)
print("\n")

# reverse() Function - reversing the elements of the list
# Syntax :- list.reverse()
print("6. reverse() - reversing the elements of the list")
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Days list:- {days_of_week}")
days_of_week.reverse()
print(days_of_week)
print("\n")

# sort() Function - it sorts the list in to some order by default in ascending order
# Syntax :- list.sort()
print("7. sort() - it sorts the list in to some order by default in ascending order")
nums = [4, 9, 1, 8, 0, 2]
print(f"Number list:- {nums}")
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print("\n")

# count() Function - it counts particular element in the list that how many times this element is present
# Syntax :- list.count(item)
print("8. count() - it counts particular element in the list that how many times this element is present")
nums = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"Number List:- {nums}")
items_to_count = int(input("Enter the number to be counted from the above list: "))
print(f"Occurrence of {items_to_count} is {nums.count(items_to_count)}")
