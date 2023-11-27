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

def add_two_to_target(numbers, target):
    if not numbers:
        return None
        print("Input is empty")
    head = 0
    tail = len(numbers) - 1
    while head < tail:
        result = numbers[head] + numbers[tail]
        if result == target:
            break
        else:
            if result > target:
                tail -= 1
            else:
                head += 1

    return [head+1, tail+1]

items = [1, 2, 3, 14, 5]
indices = add_two_to_target(items, 7)
if indices:
    print(indices)
else:
    print("No two indices match the target, sorry !!!")
