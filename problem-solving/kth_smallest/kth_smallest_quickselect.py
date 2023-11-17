from random import randint

def partition(array, start, end):
    pivot_index = randint(start, end)
    pivot_element = array[pivot_index]

    array[pivot_index], array[end] = array[end], array[pivot_index]

    less_than_pointer = start
    for idx in range(start, end):
        if array[idx] < pivot_element:
            array[idx], array[less_than_pointer] = array[less_than_pointer], array[idx]
            less_than_pointer += 1
    array[end], array[less_than_pointer] = array[less_than_pointer], array[end]

    return less_than_pointer

def quickselect(array, start, end, k):
    if start == end:
        return array[start]

    pivot_index = partition(array, start, end)
    # 3rd smallest would be at index 2 (0, 1, 2)
    kth_index = k - 1

    if kth_index == pivot_index:
        return array[kth_index]
    # k is smaller, so the element must be in the left sublist
    elif kth_index < pivot_index:
        return quickselect(array, start, pivot_index-1, kth_index)
    else:
        return quickselect(array, pivot_index+1, end, kth_index)

# test
items = [7, 3, 4, 10, 20, 15]
k = 3
kth_smallest = quickselect(items, 0, len(items) - 1, k)
print(f"{k = }, {kth_smallest = }")