# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_kval_from_end(self, head, k):
        slow = head
        fast = head

        for pos in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = self.get_kval_from_end(head, k)

        start = head
        for pos in range(k-1):
            start = start.next

        value_at_k = start.val
        
        start.val = slow.val
        slow.val = value_at_k

        return head