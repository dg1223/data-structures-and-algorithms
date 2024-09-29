'''
BST methods:
initialize, insert, search value, dfs traversal
-> if value_to_add == parent_node, add it to 
   the right child

*No need to learn to remove a node from a BST.
We generally use it to search for a value.
'''
class BST:
	def __init__(self, value, depth=0):
		self.value = value
		self.depth = depth
		self.left = None
		self.right = None

	def insert_value(self, value):
		if value < self.value:
			if not self.left:
				self.left = BST(value, self.depth+1)
				print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
			else:
				self.left.insert_value(value)
		else:
			if not self.right:
				self.right = BST(value, self.depth+1)
				print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
			else:
				self.right.insert_value(value)

	def get_node_by_value(self, value):
		if value == self.value:
			return self
		# if left child exists and 
  		# search value < current node's value
		elif self.left and value < self.value:
			self.left.get_node_by_value(value)
		elif self.right and value > self.value:
			self.right.get_node_by_value(value)

	def dfs_inorder_traversal(self):
		# traversing left will also print the root node upon return
		if self.left:
			self.left.dfs_inorder_traversal()
   
		print(f"Depth = {self.depth}, Value = {self.value}")
  
		if self.right:
			self.right.dfs_inorder_traversal()

# Test
# 	   48
# 	  /  \
# 	24    55
# 	  \      \
# 	  26     56
# 	    \        \
# 	    38       74

tree = BST(48)
tree.insert_value(24)
tree.insert_value(55)
tree.insert_value(26)
tree.insert_value(38)
tree.insert_value(56)
tree.insert_value(74)

# Print depth-first traversal:
tree.dfs_inorder_traversal()