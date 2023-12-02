class TreeNode:
	def __init__(self, value=0, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def invert_tree(self, root):
		if not root:
			return root

		self.invert_tree(root.left)
		self.invert_tree(root.right)

		root.left, root.right = root.right, root.left

		return root