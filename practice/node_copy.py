class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next_node(self, next):
        self.next = next

instance1 = Node("some value")
instance2 = Node("some other value")

instance1.set_next_node(instance2)
instance2_next_node_data = instance1.next.value

print(instance1)
print(instance1.value)
print(instance1.next)
print(instance2_next_node_data)