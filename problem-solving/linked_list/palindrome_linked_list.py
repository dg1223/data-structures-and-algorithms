# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
We need to have the first half of the list reversed
and the slow pointer to be on mid+1. Then, we just
compare the pointers as we iterate through the next
nodes
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reverse_head = None

        while fast and fast.next:
            current = slow
            slow = slow.next
            fast = fast.next.next

            current.next = reverse_head
            reverse_head = current

        # odd number of input nodes
        if fast:
            slow = slow.next

        while reverse_head and reverse_head.val == slow.val:
            reverse_head = reverse_head.next
            slow = slow.next

        return not reverse_head