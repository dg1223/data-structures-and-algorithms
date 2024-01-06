# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter_of_tree_recursive(root)

        return self.diameter

    def diameter_of_tree_recursive(self, root):
        if not root:
            return 0

        left = self.diameter_of_tree_recursive(root.left)
        right = self.diameter_of_tree_recursive(root.right)

        diameter_of_current_node = left + right
        self.diameter = max(self.diameter, diameter_of_current_node)

        return 1 + max(left, right)