# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0

        queue = deque()
        queue.append(root)

        while queue:
            current = queue.pop()
            curent_value = current.val

            if curent_value >= low and curent_value <= high:
                sum += curent_value
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return sum