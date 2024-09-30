class MinHeap:
    def __init__(self, heap=None):
        self.heap = heap

        if not heap:
            self.heap = []
            self.count = 0
        else:
            self.count = len(self.heap) - 1

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return (index * 2) + 1

    def add(self, element):
        '''
        increment count
        append item
        heapify up
        '''
        self.count += 1
        print("Adding {0} to {1}\n".format(element, self.heap))
        self.heap.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        
        # the element that was added is the last element
        cur_idx = self.count
        parent_idx = self.parent_idx(cur_idx)

        # heapify up until root node is reached
        while parent_idx >= 0:
            parent = self.heap[parent_idx]
            child = self.heap[cur_idx]
            if parent > child:
                # swap parent<>child
                print(f"swapping {parent} with {child}")
                self.heap[parent_idx] = child
                self.heap[cur_idx] = parent
                print(f"current heap list: {self.heap}\n")
                cur_idx = parent_idx
                parent_idx = self.parent_idx(cur_idx)
            else:
                break            
        print("HEAP RESTORED! {0}".format(self.heap))

# test
heap = [10, 13, 21, 22, 23, 61, 99]
min_heap = MinHeap(heap)
print(f"initial heap list: {min_heap.heap}")
print(f"intial count = {min_heap.count}\n")

#print("the parent index of 4 is:")
#print(max_heap.parent_index(4))

#print("the left child index of 3 is:")
#print(max_heap.left_child_index(3))

min_heap.add(5)