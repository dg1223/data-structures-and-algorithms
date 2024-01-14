# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_array = []
        self.bst_to_array(root, sorted_array)

        head = 0
        tail = len(sorted_array) - 1

        while head < tail:
            result = sorted_array[head] + sorted_array[tail]
            if result == k:
                return True
            elif result < k:
                head += 1
            else:
                tail -= 1

        return False
        
    def bst_to_array(self, root, array):
        if not root:
            return None

        self.bst_to_array(root.left, array)
        array.append(root.val)
        self.bst_to_array(root.right, array)