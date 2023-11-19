class Stack:
	def __init__(self, max_size=1000):
		self.items = []
		self.size = 0
		self.max_size = max_size

	def push(self, item):
		if self.has_space():
			print(f"Adding {item} to the pizza stack!")
			self.items.append(item)
			self.size += 1
		else:
			print("No space left to push")

	def pop(self):
		if not self.is_empty():
			print(f"Delivering {self.items[-1]}")
			self.size -= 1
			return self.items.pop()
		else:
			print("Nothing to remove")

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			print("Nothing remaining to see")

	def has_space(self):
		return self.size < self.max_size

	def is_empty(self):
		return self.size == 0

'''
Uncomment the following lines to test
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