# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge
        if not head:
            return None

        # base
        if not head.next:
            return head

        new_head = self.reverse_ll_recursive(head, None)
        
        return new_head

    def reverse_ll_recursive(self, head, prev):
        # base
        if not head:
            return prev

        new_head = self.reverse_ll_recursive(head.next, head)        
        head.next = prev

        return new_head
