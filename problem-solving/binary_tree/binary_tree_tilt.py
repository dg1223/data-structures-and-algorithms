# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.findTiltRecursive(root)
        return self.tilt

    def findTiltRecursive(self, root):
        if not root:
            return 0

        left = self.findTiltRecursive(root.left)
        right = self.findTiltRecursive(root.right)

        tilt_of_current_node = abs(left - right)
        self.tilt += tilt_of_current_node

        return left + right + root.val