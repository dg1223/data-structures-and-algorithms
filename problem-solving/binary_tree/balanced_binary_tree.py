# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_if_balanced(root).is_tree_balanced

    def check_if_balanced(self, root):
        # base case
        if not root:
            return BalancedWithHeight(True, -1)
        
        left_subtree = self.check_if_balanced(root.left)
        if not left_subtree.is_tree_balanced:
            # Basically, we just want the False value from here but
            # we need to return the tree object so that the return
            # statement of is_balanced() do not throw an error
            return left_subtree

        right_subtree = self.check_if_balanced(root.right)
        if not right_subtree.is_tree_balanced:
            return right_subtree

        subtree_is_balanced = abs(left_subtree.height - right_subtree.height) <= 1
        height = max(left_subtree.height, right_subtree.height) + 1

        return BalancedWithHeight(subtree_is_balanced, height)

class BalancedWithHeight:
    def __init__(self, balanced, height):
        self.is_tree_balanced = balanced
        self.height = height