'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''

def add_to_target(items, target):
    hashmap = {}
    for idx, item in enumerate(items):
        # x + y = target
        # y = target - x
        complement = target - item
        if complement in hashmap:
            return hashmap[complement], idx
        hashmap[item] = idx

items = [3, 2, 4]
indices = add_to_target(items, 6)
if indices:
    print(indices)
else:
    print("No two indices match the target, sorry !!!")
