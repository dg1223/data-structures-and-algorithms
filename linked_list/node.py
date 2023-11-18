class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# instance1 = Node("some value")
# instance2 = Node("some other value")

# instance1.set_next_node(instance2)

# instance2_next_node_data = instance1.get_next_node().get_value()

# print(instance1)
# print(instance1.get_value())
# print(instance1.get_next_node)
# print(instance2_next_node_data)