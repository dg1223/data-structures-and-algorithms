'''
Stacks using linked list
'''
from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        if self.has_space():
            print(f"Adding {value} to the pizza stack!")
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No space left to push")

    def pop(self):
        if not self.is_empty():            
            item_to_remove = self.top_item
            print(f"Delivering {item_to_remove.value}")
            self.top_item = item_to_remove.next_node
            self.size -= 1
            return item_to_remove.value
        else:
            print("Nothing to remove")

    def peek(self):
        if not self.is_empty():
            return self.top_item.value
        else:
            print("Nothing to see")


    # helper functions

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

'''
Uncomment the following lines to test
'''
# # Defining an empty pizza stack
# pizza_stack = Stack(6)
# # Adding pizzas as they are ready until we have 
# pizza_stack.push("pizza #1")
# pizza_stack.push("pizza #2")
# pizza_stack.push("pizza #3")
# pizza_stack.push("pizza #4")
# pizza_stack.push("pizza #5")
# pizza_stack.push("pizza #6")

# # Uncomment the push() statement below:
# pizza_stack.push("pizza #7")

# # Delivering pizzas from the top of the stack down
# print("The first pizza to deliver is " + pizza_stack.peek())
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()

# # Uncomment the pop() statement below:
# pizza_stack.pop()