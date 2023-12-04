'''
Assuming no stack or queue overflow will occur
based on the how the contraints are set

Time: O(N) push, O(1) pop
Space: O(N)
'''

class MyQueue:
    def __init__(self):
        self.queue_as_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        while not self.empty():
            popped_item = self.queue_as_stack.pop()
            self.stack.append(popped_item)

        self.queue_as_stack.append(x)

        while not len(self.stack) == 0:
            popped_item = self.stack.pop()
            self.queue_as_stack.append(popped_item)

    def pop(self) -> int:
        if not self.empty():
            return self.queue_as_stack.pop()

    def peek(self) -> int:
        if not self.empty():
            return self.queue_as_stack[-1]

    def empty(self) -> bool:
        return not self.queue_as_stack

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
print(f"peek: {param_3}")
param_2 = obj.pop()
print(f"pop: {param_2}")
param_4 = obj.empty()
print(f"{param_4 = }")