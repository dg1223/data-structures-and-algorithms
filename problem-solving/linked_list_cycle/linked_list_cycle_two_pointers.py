# O(N) time, O(1) and space
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_pointer = head
        slow_pointer = head

		# If there's no cycle, fast pointer will reach
		# null value first
        while fast_pointer and fast_pointer.next:			
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True
        
        return False