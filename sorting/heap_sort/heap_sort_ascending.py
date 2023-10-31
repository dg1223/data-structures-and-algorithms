from min_heap_priority_queue import MinheapQ

def heapsort(items):
    sorted_list = []
    minheap = MinheapQ()

    # create the min-heap
    for item in items:
        minheap.add(item)

    print(f"min-heap: {minheap.heaplist}")
    while minheap.position > 0:
        min_value = minheap.retrieve_min()
        sorted_list.append(min_value)

    return sorted_list

my_list = [99, 22, 61, 10, 21, 13, 23]
print(f"unsorted list = {my_list}")
print(f"sorted list = {heapsort(my_list)}")