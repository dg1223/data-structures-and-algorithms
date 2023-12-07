# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        prev = None

        while current:
			# remember: p c n
			# shift them by 1 node on every iteration
			# exception: current.next = prev
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev