'''
Algorithm:
    pivot
    divide
    combine
'''

from random import randint

def partition(items, start, end):
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

    return less_than_pointer

def quicksort(items, start, end):
    '''
    In the quicksort algorithm, the idea is to recursively sort sublists. 
    The condition if start < end: checks whether the sublist has more than 
    one element. If start is equal to or greater than end, it means the 
    sublist has zero or one element, and there's no need to sort it further 
    because a list with zero or one element is already sorted.
    '''
    if start < end:
        pivot = partition(items, start, end)
    
        ''' recursively sort left and right sub-lists '''
        quicksort(items, start, pivot - 1)
        quicksort(items, pivot + 1, end)

# sort
my_list = [4, 3, 8, 7, 1, 6, 5, 2]
print("BEFORE: ", my_list)

'''
Subtracting 1 from the end because we only need to iterate
until we reach the last element. We don't need to iterate
over the pivot element.
'''
quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", my_list)