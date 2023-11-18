class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

	def set_next_node(self, next_node):
		self.next_node = next_node

class LinkedList:
	def __init__(self, value=None):
		self.head = Node(value)

	def insert_beginning(self, value):
		new_node = Node(value)
		new_node.set_next_node(self.head)
		self.head = new_node

	def stringify_list(self):
		string = ""
		current_node = self.head
		if not current_node:
			print("No items in linked list")
			return None
		while current_node:
			current_node_value = current_node.value
			string += str(current_node_value) + "\n"
			current_node = current_node.next_node
		return string

	def remove_node(self, target_value):
		current_node = self.head
		if current_node and current_node.value == target_value:
			self.head = current_node.next_node
			return None
		while current_node:
			next_node = current_node.next_node
			if next_node and next_node.value == target_value:
				current_node.set_next_node(next_node.next_node)
				return None
			current_node = next_node

	def remove_nodes_with_same_value(self, target_value):
		current_node = self.head
		while current_node and current_node.value == target_value:
			self.head = current_node.next_node
			current_node = self.head
		while current_node:
			next_node = current_node.next_node
			if next_node and next_node.value == target_value:
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