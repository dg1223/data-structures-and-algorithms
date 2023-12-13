# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None if not head else head
        current = head
        next = current.next
        while next:
            if next.val == current.val:
                current.next = current.next.next
                next.next = None
            if current.next and current.val == current.next.val:
                next = current.next
            else:
                current = current.next
                next = current.next if current else None

        return head