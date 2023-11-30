# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self, value=None):
        self.head = ListNode()
        
    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1 and not head2:
            return None
        
        if not head1 or not head2:
            return head1 if not head2 else head2

        result = LinkedList()
        while head1 and head2:
            head1_val = head1.val
            head2_val = head2.val
            if head1_val <= head2_val:
                result.append(head1_val)
                head1 = head1.next
            else:
                result.append(head2_val)
                head2 = head2.next

        while head1:
            result.append(head1.val)
            head1 = head1.next

        while head2:
            result.append(head2.val)
            head2 = head2.next

        # skip None from beginning
        return result.head.next

