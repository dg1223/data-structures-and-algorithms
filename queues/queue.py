from node import Node

class Queue:
    def __init__(self, limit=1000):
        self.head = None
        self.tail = None
        self.size = 0
        self.limit = limit

    def enqueue(self, value):
        if self.has_space():
            item = Node(value)
            print("Adding " + str(item.value) + " to the queue!")
            if self.is_empty():
                self.head = item
                self.tail = item
            else:
                self.tail.set_next_node(item)
                self.tail = item
            self.size += 1
        else:
            print("Sorry, no space to add item")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing "  + str(item_to_remove.value) + " from the queue!")
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.next_node
                
            self.size -= 1
            return item_to_remove.value
        else:
            print("Nothing to remove")

    def peek(self):
        if not self.is_empty():
            return self.head.value
        else:
            print("Nothing to show")

    # helper functions
    
    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

'''
Uncomment the following lines to test
'''
# print("Creating a deli line with up to 10 orders...\n------------")
# deli_line = Queue(10)
# print("Adding orders to our deli line...\n------------")
# deli_line.enqueue("egg and cheese on a roll")
# deli_line.enqueue("bacon, egg, and cheese on a roll")
# deli_line.enqueue("toasted sesame bagel with butter and jelly")
# deli_line.enqueue("toasted roll with butter")
# deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
# deli_line.enqueue("two fried eggs with home fries and ketchup")
# deli_line.enqueue("egg and cheese on a roll with jalapeos")
# deli_line.enqueue("plain bagel with plain cream cheese")
# deli_line.enqueue("blueberry muffin toasted with butter")
# deli_line.enqueue("bacon, egg, and cheese on a roll")

# # Uncomment the line below:
# deli_line.enqueue("western omelet with home fries")

# print("------------\nOur first order will be " + deli_line.peek())
# print("------------\nNow serving...\n------------")
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()

# # Uncomment the line below:
# deli_line.dequeue()
