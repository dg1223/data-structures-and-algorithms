from node_copy import Node

class Queue:
    def __init__(self, limit=1000):
        self.head = None
        self.tail = None
        self.size = 0
        self.limmit = limit

    def enqueue(self, value):

    def has_space(self):
        return self.size < self.limit