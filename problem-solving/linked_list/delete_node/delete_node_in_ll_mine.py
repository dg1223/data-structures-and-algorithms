# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# No trace of intelligence here, only dumbness
# Didn't understand what the question actually wanted
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:            
            node.val = node.next.val
            if not node.next.next:
                node.next = node.next.next
                break
            node = node.next