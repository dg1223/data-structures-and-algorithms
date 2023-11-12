'''
Algorithm:
    pivot
    divide
    combine
'''

from random import randint

def quicksort(items, start, end):
    ''' base case: this portion of list has been sorted '''
    if start >= end:
        return items

    ''' select random element to be pivot '''
    pivot_index = randint(start, end)
    pivot_element = items[pivot_index]

    ''' swap random element with last element in sub-lists '''
    items[end], items[pivot_index] = items[pivot_index], items[end]

    ''' tracks all elements which should be on the left (lesser than) of pivot '''
    less_than_pointer = start
    for idx in range(start, end):
        ''' we found an element that is smaller than pivot. Swap it with lesser element '''
        if items[idx] < pivot_element:
            items[less_than_pointer], items[idx] = items[idx], items[less_than_pointer]
            ''' tally that we have one more lesser element '''
            less_than_pointer += 1
    '''
    Switch pivot element with the element at lesser than pointer (LTP)
    After this, what we'll end up with is every element before pivot is smaller 
    than it and every element after it is larger.
    '''    
    items[less_than_pointer], items[end] = items[end], items[less_than_pointer]

    ''' recursively sort left and right sub-lists '''
    left_sublist_start = start
    left_sublist_end = less_than_pointer - 1
    quicksort(items, left_sublist_start, left_sublist_end)

    right_sublist_start = less_than_pointer + 1
    right_sublist_end = end
    quicksort(items, right_sublist_start, right_sublist_end)
    
my_list = [4, 3, 8, 7, 1, 6, 5, 2]
print("BEFORE: ", my_list)
start = 0
'''
Subtracting 1 from the end because we only need to iterate
until we reach the last element. We don't need to iterate
over the pivot element.
'''
end = len(my_list) - 1
quicksort(my_list, start, end)
print("AFTER: ", my_list)