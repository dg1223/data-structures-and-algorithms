class Stack:
    def __init__(self, max_size=1000):
        self.items = []
        self.size = 0
        self.max_size = max_size	

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.max_size

    def push(self, value):
        if self.has_space():
            self.items.append(value)
            self.size += 1

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            self.size -= 1
            return popped_item
        
    def peek(self):
        if not self.is_empty():
            peeked_item = self.items[-1]
            return peeked_item


class MyQueue:
    def __init__(self, max_size=1000):
        self.queue = Stack(max_size)
        self.items = self.queue.items
        self.size = self.queue.size
        self.max_size = self.queue.max_size

    def push(self, x: int) -> None:
        stack = Stack()

        while not self.queue.is_empty():
            popped_item = self.queue.pop()
            stack.push(popped_item)

        self.queue.push(x)

        while not stack.is_empty():
            popped_item = stack.pop()
            self.queue.push(popped_item)

    def pop(self) -> int:
        popped_item = self.queue.pop()
        if popped_item:
            return popped_item

    def peek(self) -> int:
        peeked_item = self.queue.peek()
        if peeked_item:
            return peeked_item

    def empty(self) -> bool:
        return self.queue.size == 0        


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