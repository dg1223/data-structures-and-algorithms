class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    # setter
    def set_next_node(self, next_node):
        self.next_node = next_node
