from node_copy import Node

class Stack:
    def __init__(self, limit=1000):
        self.top = None
        self.limit = limit
        self.size = 0

    def push(self, value):        
        if self.has_space():
            print(f"Adding {value} to the pizza stack!")
            item = Node(value)
            if self.is_empty():
                self.top = item
            else:
                item.set_next_node(self.top)
                self.top = item
            self.size += 1
        else:
            print("No more space left in stack")

    def pop(self):
        if self.is_empty():
            print("Nothing to pop")
        else:
            item_to_remove = self.top
            print(f"Delivering {item_to_remove.value}")
            self.top = item_to_remove.next
            self.size -= 1
            return item_to_remove.value

    def peek(self):
        if self.is_empty():
            print("Nothing to see")
        else:
            return self.top.value

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

'''
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
'''