'''
Algorithm:
    divide
    sort
    merge
'''

def merge_sort(items):
    length = len(items)
    if length <= 1:
        return items
    left, right = partition(items, length)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def partition(items, length):
    mid_index = length // 2
    left_split = items[:mid_index]
    right_split = items[mid_index:]
    
    return left_split, right_split

def merge(left, right):
    result = []
    while left and right:
        left_item = left[0]
        right_item = right[0]
        if left_item < right_item:
            result.append(left_item)
            left.pop(0)
        else:
            result.append(right_item)
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

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