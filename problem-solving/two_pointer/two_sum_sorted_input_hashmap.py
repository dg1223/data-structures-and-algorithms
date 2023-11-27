'''
Given a 1-indexed array of integers numbers that is already 
sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. Let these two 
numbers be numbers[index1] and numbers[index2] where 
1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.
'''

def add_to_target(numbers, target):
    hashmap = {}
    for idx, item in enumerate(numbers):
        # x + y = target
        # y = target - x
        complement = target - item
        if complement in hashmap:
            return [hashmap[complement]+1, idx+1]
        hashmap[item] = idx

items = [1, 2, 3, 4, 5]
indices = add_to_target(items, 6)
if indices:
    print(indices)
else:
    print("No two indices match the target, sorry !!!")
