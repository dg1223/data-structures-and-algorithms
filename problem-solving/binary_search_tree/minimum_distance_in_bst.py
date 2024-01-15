import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_array = []
        self.sort_bst(root, sorted_array)

        min_abs_diff = math.inf

        # compare neighbouring elements
        '''
        For each item in a sorted array, the distance between it and
        and its adjacent item is always smaller than that of 
        its non-adjacent items
        '''
        for idx, num in enumerate(sorted_array):
            if idx == len(sorted_array) - 1:
                break
            difference = abs(sorted_array[idx] - sorted_array[idx+1])
            if difference < min_abs_diff:
                min_abs_diff = difference

        return min_abs_diff


    def sort_bst(self, root, array):
        if not root:
            return None

        self.sort_bst(root.left, array)
        array.append(root.val)
        self.sort_bst(root.right, array)

        
        