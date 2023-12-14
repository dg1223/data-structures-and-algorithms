# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:		
        current = head
        size = 0
        while current:
            size += 1
            current = current.next

        # remove head
        if n == size:
            head = head.next
            return head

        current = head
        num_iterations = size - n

        while num_iterations > 1:
            current = current.next
            num_iterations -= 1

        current.next = current.next.next

        return head