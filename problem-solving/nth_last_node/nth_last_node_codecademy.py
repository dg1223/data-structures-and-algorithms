from linkedlist import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  nth_last_pointer = None
  tail_pointer = linked_list.head_node
  count = 1

  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1

    if count >= n + 2:
      if nth_last_pointer is None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()
    
  return nth_last_pointer

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)

  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
# print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 2)
print(nth_last.value)