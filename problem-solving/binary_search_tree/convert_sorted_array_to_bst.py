# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBST_recursive(nums, 0, len(nums)-1)
    
    def sortedArrayToBST_recursive(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        
        current_root = TreeNode(nums[mid])
        left_subtree = self.sortedArrayToBST_recursive(nums, left, mid-1)
        right_subtree = self.sortedArrayToBST_recursive(nums, mid+1, right)
        
        current_root.left = left_subtree
        current_root.right = right_subtree
        
        return current_root