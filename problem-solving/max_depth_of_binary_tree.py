# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        depth_max = self.depth(root)

        return depth_max

    
    def depth(self, root):
        if not root:
            return 0

        left = self.depth(root.left)
        right = self.depth(root.right)

        return 1 + max(left, right)
