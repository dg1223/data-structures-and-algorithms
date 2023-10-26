class MaxheapQ:
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

    def child_present(self, index):
        return self.left_child_index(index) <= self.count

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
            if parent < child:
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

    def retrieve_max(self):
        last_index = self.count
        max_val = self.heaplist[0]
        print(f">>> Maximum value = {max_val} <<<\n")
        print("Reordering priority queue...clear")
        print(f"Removing: {max_val} from {self.heaplist}")
        self.heaplist[0] = self.heaplist[last_index]
        self.heaplist.pop()
        self.count -= 1
        print(f"{max_val} removed. Last element moved to the beginning: {self.heaplist}\n")
        self.heapify_down()

        return max_val

    def heapify_down(self):
        index = 0
        print("Heapifying down...")
        while self.child_present(index):
            print(f"Retrieving larger child index of {self.heaplist[index]}")
            larger_child_index = self.get_larger_child_index(index)
            parent = self.heaplist[index]
            child = self.heaplist[larger_child_index]
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heaplist[index] = child
                self.heaplist[larger_child_index] = parent
                print(f"current heap list: {self.heaplist}\n")
                index = larger_child_index
            else:
                break
        print("No more children exist")
        print(f"\nHEAP RESTORED! {self.heaplist}")

    def get_larger_child_index(self, index):
        if self.right_child_index(index) > self.count:
            print(f"There is only a left child of {self.heaplist[index]}")
            return self.left_child_index(index)
        else:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)
            left_child = self.heaplist[left_child_index]
            right_child = self.heaplist[right_child_index]
            if left_child > right_child:
                print(f"Left child {left_child} is larger. Picking the left child.")
                return left_child_index
            else:
                print(f"Left child {left_child} is not larger. Picking the right child {right_child}")
                return right_child_index


# test
heaplist = [99, 22, 61, 10, 21, 13, 23]
max_heap = MaxheapQ(heaplist)
print(f"initial heap list: {max_heap.heaplist}\n")

#max_heap.add(90)
max_heap.retrieve_max()