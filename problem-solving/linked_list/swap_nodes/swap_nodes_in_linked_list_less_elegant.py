# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head

        slow = head
        fast = head

        for pos in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        value_of_kth_node_from_end = slow.val

        start = head
        for pos in range(k-1):
            start = start.next

        value_at_k = start.val
        
        start.val = value_of_kth_node_from_end
        slow.val = value_at_k

        return head