'''
Algorithm:
    pivot
    divide
    combine
'''

from random import randint

def partition(items, start, end):
    pivot_index = randint(start, end)
    pivot_element = items[pivot_index]

    items[end], items[pivot_index] = items[pivot_index], items[end]

    less_than_pointer = start
    for idx in range(start, end):
        if items[idx] < pivot_element:
            items[less_than_pointer], items[idx] = items[idx], items[less_than_pointer]
            less_than_pointer += 1

    items[less_than_pointer], items[end] = items[end], items[less_than_pointer]

    return less_than_pointer

def quicksort(items, start, end):
    if start < end:
        pivot = partition(items, start, end)

        quicksort(items, start, pivot - 1)
        quicksort(items, pivot + 1, end)
    
my_list = [4, 3, 8, 7, 1, 6, 5, 2]
print("BEFORE: ", my_list)

quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", my_list)