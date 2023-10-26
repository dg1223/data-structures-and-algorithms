class Minheap:
    def __init__(self, heaplist=None):
        if not heaplist:
            self.heaplist = []
            self.count = 0
        else:
            self.heaplist = heaplist
            self.count = len(self.heaplist)-1

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def add(self, value):
        self.count += 1
        print("Adding {0} to {1}\n".format(value, self.heaplist))
        self.heaplist.append(value)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        index = self.count
        parent_index = self.parent_index(index)

        while parent_index >= 0:
            parent = self.heaplist[parent_index]
            child = self.heaplist[index]
            if parent > child:
                print(f"swapping {parent} with {child}")
                self.heaplist[parent_index] = child
                self.heaplist[index] = parent
                print(f"current heap list: {self.heaplist}\n")
                index = parent_index
                parent_index = self.parent_index(index)
            # here, we are assuming that a valid heap is provided
            # improvement -> function to check if input heap is valid
            else:                
                break
        print("Restored Heap: {0}\n".format(self.heaplist))

# test
heaplist = [10, 13, 21, 22, 23, 61, 99]
min_heap = Minheap(heaplist)
print(f"initial heap list: {min_heap.heaplist}")
print(f"intial count = {min_heap.count}\n")

min_heap.add(5)