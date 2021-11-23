'''
Author: Shamir Alavi
Date: 2021-11-22
Topic: Linked List (singly linked)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CountNodes:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodes(self, data):
        newNode = Node(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def countNodes(self):
        current = self.head
        count = 0

        while (current != None):
            current = current.next
            count += 1

        return count

    def display(self):
        current = self.head

        if (current == None):
            print("List is empty")
            return

        print("Displaying the content of the nodes in the singly linked list")
        while (current != None):
            print(current.data)
            current = current.next
