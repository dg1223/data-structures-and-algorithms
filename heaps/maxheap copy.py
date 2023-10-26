class MaxHeap:
    def __init__(self, heap_list=None):
        self.heap_list = heap_list

        if not heap_list:
            self.heap_list = []
            self.count = 0
        else:
            self.count = len(self.heap_list) - 1

    def parent_index(self, index):
        return (index-1) // 2

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def add(self, element):
        '''
        increment count
        add element to heap list
        reorder the heap
        '''
        self.count += 1
        print("Adding {0} to {1}\n".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        # the element that was added is the last element
        index = self.count
        parent_index = self.parent_index(index)

        while parent_index > 0: # index 0 has None
            parent = self.heap_list[parent_index]
            child = self.heap_list[index]
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[parent_index] = child
                self.heap_list[index] = parent
                print(f"current heap list: {self.heap_list}\n")
            index = parent_index
            parent_index = self.parent_index(index)
            
        print("HEAP RESTORED! {0}".format(self.heap_list))

# test
heap_list = [99, 22, 61, 10, 21, 13, 23]
max_heap = MaxHeap(heap_list)
print(f"initial heap list: {max_heap.heap_list}")
print(f"intial count = {max_heap.count}\n")

#print("the parent index of 4 is:")
#print(max_heap.parent_index(4))

#print("the left child index of 3 is:")
#print(max_heap.left_child_index(3))

max_heap.add(90)