from node_copy import Node

class LinkedList:
    def __init__(self, value=None):
        '''
        There will always be a head node so that
        linked list is never empty upon initialization
        '''
        self.head = Node(value)

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def stringify(self):
        string = ""
        current_node = self.head
        while current_node:
            print(f"current node: {current_node.value}")
            # Skip printing nodes that were removed
            if current_node.value != None:
                string += str(current_node.value) + "\n"
                current_node = current_node.next
        '''        
        Don't print here. Otherwise, the script that calls
        this function will print None in the output
        '''
        return string

    # remove node with the 1st occurence of target value
    def remove_node(self, value):
        current_node = self.head

        if current_node.value == value:
            self.head = current_node.next
            return

        next_node = current_node.next        
        while next_node:
            if next_node.value == value:
                current_node.set_next_node(next_node.next)
                return
            next_node = next_node.next

    def remove_nodes_with_same_value(self, value):
        current_node = self.head
        
        # original head has the value to remove
        while current_node.value == value:
            next_node = current_node.next
            self.head = next_node
            current_node = next_node

        # current_node doesn't change if original head is not removed
        next_node = current_node.next
        while next_node:
            if next_node.value == value:
                current_node.set_next_node(next_node.next)
            next_node = next_node.next

# Test your code
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(70)
print(ll.stringify())
#ll.remove_nodes_with_same_value(70)
#print(ll.stringify())
        