class MinheapQ:
    def __init__(self, heaplist=None):
        if heaplist is not None:
            self.heaplist = heaplist
            self.count = len(heaplist)
            self.build_heap()
        else:
            self.heaplist = []
            self.count = 0

    def build_heap(self):
        for i in range(self.count // 2, -1, -1):
            self.heapify_down(i)

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def child_present(self, index):
        return self.left_child_index(index) < self.count

    def add(self, value):
        self.heaplist.append(value)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.count - 1
        while index > 0:
            parent_index = self.parent_index(index)
            if self.heaplist[index] < self.heaplist[parent_index]:
                self.heaplist[index], self.heaplist[parent_index] = self.heaplist[parent_index], self.heaplist[index]
            else:
                break
            index = parent_index

    def retrieve_min(self):
        if self.count == 0:
            print("No more items in heap")
            return None

        min_value = self.heaplist[0]
        self.heaplist[0] = self.heaplist[self.count - 1]
        self.count -= 1
        self.heapify_down(0)

        return min_value

    def heapify_down(self, index):
        while self.child_present(index):
            smaller_child_index = self.get_smaller_child_index(index)
            if self.heaplist[index] > self.heaplist[smaller_child_index]:
                self.heaplist[index], self.heaplist[smaller_child_index] = self.heaplist[smaller_child_index], self.heaplist[index]
            else:
                break
            index = smaller_child_index

    def get_smaller_child_index(self, index):
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        if right_child_index >= self.count or self.heaplist[left_child_index] < self.heaplist[right_child_index]:
            return left_child_index
        else:
            return right_child_index

## Test
#heaplist = [10, 13, 21, 22, 99]
#min_heap = MinheapQ(heaplist)
#print(f"initial heap list: {min_heap.heaplist}\n")
#
#number = 90
#min_heap.add(number)
#print(f"heap list after adding {number}: {min_heap.heaplist}\n")
#
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
#print(f"minimum value = {min_heap.retrieve_min()}")
