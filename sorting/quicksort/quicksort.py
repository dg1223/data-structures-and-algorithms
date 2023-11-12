'''
Algorithm:
    pivot
    divide
    combine
'''

from random import randint

def quicksort(items, start, end):
    if start >= end:
        return items
    pivot_index = randint(start, end)
    pivot_element = items[pivot_index]

    items[end], items[pivot_index] = items[pivot_index], items[end]

    less_than_pointer = start
    for idx in range(start, end):
        if items[idx] < pivot_element:
            items[less_than_pointer], items[idx] = items[idx], items[less_than_pointer]
            less_than_pointer += 1

    items[less_than_pointer], items[end] = items[end], items[less_than_pointer]

    left_sublist_start = start
    left_sublist_end = less_than_pointer - 1
    quicksort(items, left_sublist_start, left_sublist_end)

    right_sublist_start = less_than_pointer + 1
    right_sublist_end = end
    quicksort(items, right_sublist_start, right_sublist_end)
    
my_list = [4, 3, 8, 7, 1, 6, 5, 2]
print("BEFORE: ", my_list)

quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", my_list)