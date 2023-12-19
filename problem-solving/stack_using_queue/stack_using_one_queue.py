from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self.size += 1        

    def pop(self) -> int:
		'''
		Cannot use a while loop and decrement size
		because size should be decremented only when
		an item is popped
		'''
        for _ in range(self.size - 1):
            self.q.appendleft(self.q.pop())

        self.size -= 1
        return self.q.pop()

    def top(self) -> int:        
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()