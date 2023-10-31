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
        print(f"{index = }")
        print(f"left child index = {self.left_child_index(index)}")
        print(f"count = {self.count}")
        return self.left_child_index(index) < self.count

    # add() and heapify_up() not required if not adding anything to list
    def add(self, value):
        self.heaplist.append(value)
        print(f"current heaplist: {self.heaplist}")
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        # we need to start from index 0
        index = self.count - 1
        print(f"{index = }")
        parent_index = self.parent_index(index)
        #print(f"parent index before loop = {parent_index}")

        '''
        While adding items to an empty list, the first element
        aka the root does not have any children. So, we skip it.
        ''' 
        while parent_index >= 0:
            parent = self.heaplist[parent_index]
            child = self.heaplist[index]
            if parent > child:
                self.heaplist[parent_index] = child
                self.heaplist[index] = parent
            index = parent_index
            parent_index = self.parent_index(index)
            #print(f"parent index after loop = {parent_index}")

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return

        print("\nretrieving min...")

        last_index = self.count - 1
        #print(f"{last_index = }")
        min_value = self.heaplist[0]
        print(f"{min_value = }")
        print(f"heaplist = {self.heaplist}")
        self.heaplist[0] = self.heaplist[last_index]
        print(f"heaplist after swapping = {self.heaplist}")
        self.heaplist.pop()
        print(f"heaplist after popping = {self.heaplist}")
        self.count -= 1
        self.heapify_down()
        print(f"adding {min_value = } to sorted list")
        
        return min_value

    def heapify_down(self):
        index = 0
        while self.child_present(index):
            print("child is present...")
            print("inside while loop...")
            smaller_child_index = self.get_smaller_child_index(index)
            print(f"{smaller_child_index = }")
            parent = self.heaplist[index]
            child = self.heaplist[smaller_child_index]
            print(f"{parent = }, {child = }")
            if parent > child:
                self.heaplist[index] = child
                self.heaplist[smaller_child_index] = parent
            print(f"heaplist after swapping = {self.heaplist}")
            index = smaller_child_index
            print(f"{index = }")

    def get_smaller_child_index(self, index):
        print(f"\nheaplist = {self.heaplist}")
        print(f"parent index = {index}")
        print(f"count = {self.count}")
        print(f"{self.right_child_index(index) = }")
        if self.right_child_index(index) > self.count - 1:
            print(f"no right child present. returning left child...")
            return self.left_child_index(index)
        else:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)
            print(f"{left_child_index = }, {right_child_index = }")
            left_child = self.heaplist[left_child_index]
            right_child = self.heaplist[right_child_index]
            print(f"{left_child = }, {right_child = }")
            
            if right_child < left_child:
                return right_child_index
            else:
                return left_child_index

'''
# test
heaplist = [10, 13, 21, 22, 23, 61, 99]
min_heap = MinheapQ(heaplist)
print(f"initial heap list: {min_heap.heaplist}\n")

#max_heap.add(90)
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
print(f"minimum value = {min_heap.retrieve_min()}")
'''