class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class LinkedList:
    def __init__(self, value=None):
        self.head = ListNode(value)

    def append(self, value):
        new_node = ListNode(value)
            
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
         
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
         
    def reverseList(self, head):
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
      
    def stringify_list(self, head):
        string = ""
        current_node = head
        if not current_node:
            print("Linked list is empty")
        
        while current_node:
            current_node_value = current_node.val
            if current_node_value is not None:
                string += str(current_node_value) + "\n"
            current_node = current_node.next
        
        return string

# Test your code
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

new_head = ll.reverseList(ll.head)

print(ll.stringify_list(new_head))
