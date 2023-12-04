class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.peek()            
        return self.stack_2.pop()

    def peek(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        
        return self.stack_2[-1]        

    def empty(self) -> bool:
        return not self.stack_1 and not self.stack_2


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