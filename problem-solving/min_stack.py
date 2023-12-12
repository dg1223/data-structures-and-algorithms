class MinStack:
    def __init__(self, max_size=30000):
        self.items = []
        self.min_stack = []
        self.size = 0
        self.max_size = max_size
        
    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.max_size

    def push(self, value):
        if self.has_space:
            self.items.append(value)
            self.size += 1

        minimum = value
        if self.min_stack:
            minimum = min(self.min_stack[-1], value)

        self.min_stack.append(minimum)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
            self.size -= 1
        self.min_stack.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.min_stack[-1]
