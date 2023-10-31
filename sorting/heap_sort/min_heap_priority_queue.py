# Priority queue using min-heap

class MinheapQ:
    def __init__(self, heaplist=None):
        if not heaplist:
            self.heaplist = []
            self.count = 0
        else:
            self.heaplist = heaplist
            self.count = len(heaplist) - 1

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def child_present(self, index):
        return self.left_child_index(index) <= self.count

    # add() and heapify_up() not required if not adding anything to list
    def add(self, value):
        self.heaplist.append(value)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.count
        parent_index = self.parent_index(index)

        while parent_index >= 0:
            parent = self.heaplist[parent_index]
            child = self.heaplist[index]
            if parent > child:
                self.heaplist[parent_index] = child
                self.heaplist[index] = parent
            index = parent_index
            parent_index = self.parent_index(index)

    def retrieve_min(self):
        last_index = self.count
        min_value = self.heaplist[0]
        self.heaplist[0] = self.heaplist[last_index]
        self.heaplist.pop()
        self.count -= 1
        self.heapify_down()
        
        return min_value

    def heapify_down(self):
        index = 0
        while self.child_present(index):
            smaller_child_index = self.get_smaller_child_index(index)
            parent = self.heaplist[index]
            child = self.heaplist[smaller_child_index]
            if parent > child:
                self.heaplist[index] = child
                self.heaplist[smaller_child_index] = parent
            index = smaller_child_index

    def get_smaller_child_index(self, index):
        if self.right_child_index(index) > self.count:
            return self.left_child_index(index)
        else:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)
            left_child = self.heaplist[left_child_index]
            right_child = self.heaplist[right_child_index]
            
            if right_child < left_child:
                return right_child_index
            else:
                return left_child_index


# test
heaplist = [10, 13, 21, 22, 23, 61, 99]
min_heap = MinheapQ(heaplist)
print(f"initial heap list: {min_heap.heaplist}\n")

#max_heap.add(90)
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
