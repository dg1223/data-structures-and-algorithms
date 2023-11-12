'''
Algorithm:
    divide
    sort
    merge
'''

from collections import deque

def merge_sort(items):
    length = len(items)
    # base case
    if length <= 1:
        return items
    left, right = partition(items, length)
    # recursive steps
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def partition(items, length):
    mid_index = length // 2
    left_split = items[:mid_index]
    right_split = items[mid_index:]
    
    return left_split, right_split

def merge(left_sublist, right_sublist):
    result = deque()
    left = deque(left_sublist)
    right = deque(right_sublist)

    while left and right:
        left_item = left[0]
        right_item = right[0]

        if left_item < right_item:
            '''
            if you don't pop, this will become
            an infinite loop
            '''
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    '''
    If you return the raw result, the raw deque object
    gets printed which still shows all items.
    To return a list object, do:
    return list(deque)
    '''
    return result


unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print("ordered_list1\n{0}\n".format(ordered_list1))
print("ordered_list2\n{0}\n".format(ordered_list2))
print("ordered_list3\n{0}\n".format(ordered_list3))