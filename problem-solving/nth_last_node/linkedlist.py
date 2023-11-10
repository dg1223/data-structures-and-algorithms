# We'll be using our Node class
from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
        # Linked list where new values are inserted in the beginning
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        if not current_node:
            print('There are no nodes in the list')
        else:
            while current_node:
                current_node_value = current_node.get_value()
                if current_node_value != None:
                    string_list += str(current_node_value) + '\n'
                current_node = current_node.get_next_node()
        return string_list
	
	
    # remove the first node that has a specific value
    def remove_node(self, value_to_remove):
        current_node = self.head_node
	  
		# To remove the current head node,set its pointer to the next node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return
            
        while current_node:
	        next_node = current_node.get_next_node()
	        if next_node and next_node.get_value() == value_to_remove:
	            # Found the node to remove, so update the pointers
	            current_node.set_next_node(next_node.get_next_node())
	            return
	        current_node = next_node


	# remove all nodes that have the same value
    def remove_all_nodes(self, value_to_remove):
        current_node = self.head_node
        
        # Handle the case where the head node(s) have the value to remove
        while current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            current_node = self.head_node
        
        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
            else:
                current_node = next_node
