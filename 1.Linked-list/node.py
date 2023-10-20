class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def get_link_node(self):
        return self.link_node
    
    def get_value(self):
        return self.value

instance1 = Node("some value")
instance2 = Node("some other value")

instance1.set_link_node(instance2)

instance2_link_node_data = instance1.get_link_node().get_value()

print(instance1)
print(instance1.get_value())
print(instance1.get_link_node)
print(instance2_link_node_data)