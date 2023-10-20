from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    # def get_head_node(self):
    #     return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string = ""
        current_node = self.head_node
        if not current_node:
            print("Linked list is empty")
        
        while current_node:
            current_node_value = current_node.value
            if current_node_value is not None:
                string += str(current_node_value) + "\n"
            current_node = current_node.get_next_node()
        
        return string

    def remove_node(self, value_to_remove):
        current_node = self.head_node

        # if target value is in head node
        if current_node and current_node.value == value_to_remove:
            self.head_node = current_node.next_node
            return
        
        # current node starts with being the head node
        while current_node:
            next_node = current_node.next_node
            if next_node and next_node.value == value_to_remove:
                current_node.set_next_node(next_node.next_node)
                return
            current_node = next_node

    def remove_nodes_with_same_value(self, value_to_remove):
        current_node = self.head_node

        # head node and its subsequent node(s) have target value
        while current_node and current_node.value == value_to_remove:
            self.head_node = current_node.next_node
            current_node = self.head_node

        while current_node:
            next_node = current_node.next_node
            if next_node and next_node.value == value_to_remove:
                current_node.set_next_node(next_node.next_node)
            current_node = next_node

# Test your code
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(70)
print(ll.stringify_list())
ll.remove_nodes_with_same_value(70)
print(ll.stringify_list())
