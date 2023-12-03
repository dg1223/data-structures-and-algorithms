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
        visited = set()
        current_node = head
        visited.add(current_node)
        while current_node:
            next_node = current_node.next
            if next_node in visited:
                return True
            visited.add(next_node)
            current_node = next_node
        
        return False 