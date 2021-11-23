'''
Author: Shamir Alavi
Date: 2021-11-22
Topic: Linked List (singly linked)
'''

import singly_linked_list

sList = singly_linked_list.CountNodes()

sList.addNodes(1)
sList.addNodes(2)
sList.addNodes(3)
sList.addNodes(4)

sList.display()
print("Number of nodes in the singly linked list = " + str(sList.countNodes()))