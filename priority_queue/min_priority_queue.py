'''
MinHeap + (child_present, retrieve_min, heapify_down)
heapify_down uses get_smaller_child_index
'''

class MinHeapQ:
    def __init__(self, heap_list=None):
        # add sentinel value if not initially added 
        if heap_list and heap_list[0] != None:
            self.heap_list = [None]
            self.heap_list += heap_list
        else:
            self.heap_list = heap_list

        if not heap_list:
            self.count = 0
        else:
            self.count = len(self.heap_list) - 1

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return (index * 2) + 1

    def child_present(self, index):
        return self.left_child_index(index) <= self.count

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
            if parent > child:
                print(f"swapping {parent} with {child}")
                self.heap_list[parent_index] = child
                self.heap_list[index] = parent
                print(f"current heap list: {self.heap_list}\n")
            index = parent_index
            parent_index = self.parent_index(index)
            
        print("HEAP RESTORED! {0}".format(self.heap_list))

    def retrieve_min(self):
        last_index = self.count
        if last_index == 0:
            print("No item in heap")
            return
        min_value = self.heap_list[1]
        print(f">>> Minimum value = {min_value} <<<\n")
        print("Reordering priority queue...")
        print(f"Removing: {min_value} from {self.heap_list}")
        self.heap_list[1] = self.heap_list[last_index]
        self.heap_list.pop()
        self.count -= 1
        print(f"{min_value} removed. Last element moved to the beginning: {self.heap_list}\n")
        self.heapify_down()

        return min_value

    def heapify_down(self):
        index = 1
        print("Heapifying down...")
        while self.child_present(index):
            print(f"Retrieving smaller child index of {self.heap_list[index]}")
            smaller_child_index = self.get_smaller_child_index(index)
            parent = self.heap_list[index]
            child = self.heap_list[smaller_child_index]
            if parent > child:
                print(f"swapping {parent} with {child}")
                self.heap_list[index] = child
                self.heap_list[smaller_child_index] = parent
                print(f"current heap list: {self.heap_list}\n")
            index = smaller_child_index
        print("No more children exist")
        print(f"\nHEAP RESTORED! {self.heap_list}")

    def get_smaller_child_index(self, index):
        if self.right_child_index(index) > self.count:
            print(f"There is only a left child of {self.heap_list[index]}")
            return self.left_child_index(index)
        else:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)
            left_child = self.heap_list[left_child_index]
            right_child = self.heap_list[right_child_index]
            if left_child < right_child:
                print(f"Left child {left_child} is smaller. Picking the left child.")
                return left_child_index
            else:
                print(f"Left child {left_child} is not smaller. Picking the right child {right_child}")
                return right_child_index

# test
heap_list = [10, 13, 21, 22, 23, 61, 99]
min_heap = MinHeapQ(heap_list)
print(f"initial heap list: {min_heap.heap_list}\n")

#min_heap.add(5)
min_heap.retrieve_min()