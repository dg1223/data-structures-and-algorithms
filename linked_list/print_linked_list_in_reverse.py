class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def set_next_node(self, next):
		self.next = next

class LinkedList:
	def __init__(self, value=None):
		self.head = Node(value)

	def insert_beginning(self, value):
		new_node = Node(value)
		new_node.set_next_node(self.head)
		self.head = new_node

	def reverse_list(self, head):
		if not head or not head.next:
			return head
		new_head = self.reverse_list(head.next)
		head.next.next = head
		head.next = None
		return new_head


	def stringify_list(self):
		string = ""
		current_node = self.head
		if not current_node:
			print("No items in linked list")
			return None
		while current_node:
			current_node_value = current_node.value
			if current_node_value is not None:
				string += str(current_node_value) + "\n"
			current_node = current_node.next
		return string

	def remove_node(self, target_value):
		current_node = self.head
		if current_node and current_node.value == target_value:
			self.head = current_node.next
			return None
		while current_node:
			next_node = current_node.next
			if next_node and next_node.value == target_value:
				current_node.set_next_node(next_node.next)
				return None
			current_node = next_node

	def remove_nodes_with_same_value(self, target_value):
		current_node = self.head
		while current_node and current_node.value == target_value:
			self.head = current_node.next
			current_node = self.head
		while current_node:
			next_node = current_node.next
			if next_node and next_node.value == target_value:
				current_node.set_next_node(next_node.next)
			current_node = next_node

# Create a linked list
ll = LinkedList()
ll.insert_beginning(3)
ll.insert_beginning(2)
ll.insert_beginning(1)

# Print the original linked list
print("Original Linked List:")
print(ll.stringify_list())

# Reverse the linked list
ll.head = ll.reverse_list(ll.head)

# Print the reversed linked list
print("\nReversed Linked List:")
print(ll.stringify_list())