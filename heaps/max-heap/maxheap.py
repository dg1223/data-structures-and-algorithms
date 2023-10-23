class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return (index * 2) + 1

    def add(self, element):
        '''
        increment count
        add element to heap list
        reorder the heap
        '''
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        # the element that was added is the last element
        index = self.count
        parent_index = self.parent_index(index)
        parent = self.heap_list[parent_index]
        child = self.heap_list[index]

        while parent_index > 0: # index 0 has None
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[parent_index] = child
                self.heap_list[index] = parent
            index = parent_index
        print("HEAP RESTORED! {0}".format(self.heap_list))

