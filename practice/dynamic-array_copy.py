'''
In Python, a list is a dynamic array. 
'''

# create
lst = []

# fill list with items
lst = [1, 2, 3]
print(f"initial list: {lst}")

# add items
lst.append(4)
print(f"list after append: {lst}")

# iterate over items
print(f"iterate over list: {lst}")
for item in lst:
    print(item)

# keep track of current index
print(f"list items with indices...")
for index, item in enumerate(lst):
    print(f"{index}: {item}")

# remove items by value
# -> removes 1st occurance of value
lst.remove(4)
print(f"list after removing 4: {lst}")

# remove item by index
del lst[0]
print(f"list after removing index 0: {lst}")

# iterate over items and modify
'''
Note: You cannot iterate over a list and modify it in-place
You have to create a slice (copy) of it and modify that instead
'''
lst = [item for item in lst[:] if item % 2 == 0 ]
print(f"items divisible by 2: {lst}")