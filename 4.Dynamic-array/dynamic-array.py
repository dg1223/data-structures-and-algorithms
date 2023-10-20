'''
In Python, a list is a dynamic array. 
'''

# create
_list = []

# fill list with items
_list = [1, 2, 3]
print(f"_list: {_list}\n")

# add items
_list.append(4)
print(f"_list: {_list}\n")

# iterate over items
_list2 = [item for item in _list]
print(f"_list2: {_list2}\n")

# keep track of current index
for index, item in enumerate(_list):
    print(f"{index}: {item}")
print()

# remove items
_list.remove(4) # removes 1st occurance of 4
del _list[0] # removes item at index 0
print(f"_list: {_list}\n")

# iterate over items and modify
'''
Note: You cannot iterate over a list and modify it in-place
You have to create a slice (copy) of it and modify that instead
'''
_list2 = [item for item in _list2[:] if item % 2 != 0]
print(f"_list2: {_list2}\n")
