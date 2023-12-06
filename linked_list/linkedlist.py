from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head)
        self.head = new_node

    # O(N) time
    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # O(1) time
    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        tail.next = new_node
        tail = new_node

    def stringify_list(self):
        string = ""
        current_node = self.head
        if not current_node:
            print("Linked list is empty")
        
        while current_node:
            current_node_value = current_node.value
            if current_node_value is not None:
                string += str(current_node_value) + "\n"
            current_node = current_node.next_node
        
        return string

    # remove the first node that contains the target value
    def remove_node(self, value_to_remove):
        current_node = self.head

        # if target value is in head node
        if current_node and current_node.value == value_to_remove:
            self.head = current_node.next_node
            return
        
        # current node starts with being the head node
        while current_node:
            next_node = current_node.next_node
            if next_node and next_node.value == value_to_remove:
                current_node.set_next_node(next_node.next_node)
                return
            current_node = next_node

    # remove all nodes that contain the target value
    def remove_nodes_with_same_value(self, value_to_remove):
        current_node = self.head

        # head node and its subsequent node(s) have target value
        while current_node and current_node.value == value_to_remove:
            self.head = current_node.next_node
            current_node = self.head

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
