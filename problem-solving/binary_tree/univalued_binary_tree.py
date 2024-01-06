# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        return self.isUnivalTreeRecursion(root, value)        

    def isUnivalTreeRecursion(self, root, value):
        if not root:
            return True

        if root.val != value:
            return False

        left = self.isUnivalTreeRecursion(root.left, value)
        right = self.isUnivalTreeRecursion(root.right, value)

        return left and right