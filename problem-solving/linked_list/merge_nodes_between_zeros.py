# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        
        while fast:
            if fast.val != 0:
                slow.val += fast.val
                fast = fast.next
                slow.next = slow.next.next
            else:
                # reached tail
                if not fast.next:
                    slow.next = slow.next.next
                    fast = fast.next
                else:
                    slow = fast
                    fast = fast.next

        return head
      