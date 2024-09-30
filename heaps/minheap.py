class MinHeap:
    def __init__(self, heap=None):
        if not heap:
            self.heap = []
            self.count = 0
        else:
            self.heap = heap
            self.count = len(heap) - 1
            
    def parent_index(self, index):
        return index // 2
    
    def left_child_index(self, index):
        return index * 2
    
    def right_child_index(self, index):
        return (index * 2) +  1
    
    def add_item(self, item):
        '''
        increment count
        append item
        heapify up
        '''
        self.count += 1
        self.heap.append(item)
        self.heapify_up()
        
    def heapify_up(self):
        cur_idx = self.count
        parent_idx = self.parent_index(cur_idx)
        
        # heapify up until root node is reached
        while parent_idx > 0:
            parent = self.heap[parent_idx]
            child = self.heap[cur_idx]
            
            # swap parent<>child
            if parent > child:
                self.heap[parent_idx] = child
                self.heap[cur_idx] = parent                
                # Now, we move further up the heap
                cur_idx = parent_idx
                parent_idx = self.parent_index(cur_idx)
            else:
                break
            
# test
heap = [10, 13, 21, 22, 23, 61, 99]
min_heap = MinHeap(heap)
print(f"initial heap list: {min_heap.heap}")
print(f"intial count = {min_heap.count}\n")

print("the parent index of 4 is:")
print(min_heap.parent_index(4))

print("the left child index of 3 is:")
print(min_heap.left_child_index(3))

min_heap.add_item(5)
print()
print(f"current heap list: {min_heap.heap}")
print(f"current count = {min_heap.count}\n")