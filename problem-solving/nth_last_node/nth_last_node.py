from linkedlist import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  # edge case 3
  if n <= 0:
    return "Invalid input for n"


  iterating_pointer = linked_list.head_node
  '''
  tracking pointer is set to None to prevent invalid input parameter n
  example: if there are only 2 items in the list, 0 & 1, but we need to
  show the 3rd last item, n = 3, is is impossible. In this case, our 
  counter will not get beyond 1. So, tracking pointer will remain None
  and we can return None.
  '''
  tracking_pointer = None
  count = 0

  # edge case 1
  '''
  iterating_pointer is not None. It is an instance of the head_node 
  whose value is None. We need to check if its initial value is None
  '''
  if iterating_pointer.value is None:
    return "Linked List is empty."

  while iterating_pointer:
    iterating_pointer = iterating_pointer.get_next_node()
    # delay tracking pointer by n indices (nodes)
    if count >= n:
      if not tracking_pointer:
        tracking_pointer = linked_list.head_node
      else:
        tracking_pointer = tracking_pointer.get_next_node()
    count += 1
  
  # edge case 2
  '''
  It will be impossible to show the value of the 3rd last node in a 
  list which only has 2 items.
  The following code can also be written as:
  if n > count:
    return "Invalid input for n"
  '''
  if not tracking_pointer:
    return "Invalid input for n"
  
  return tracking_pointer.value
    

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(3, 0, -1):
    linked_list.insert_beginning(i)

  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 10)
print(nth_last)