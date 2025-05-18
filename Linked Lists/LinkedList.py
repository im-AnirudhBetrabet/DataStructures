from wsgiref.validate import header_re

from Node import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value, end=' -> ')
            curr_node = curr_node.next
        print(None)


    '''
    :param value The Value of the new node being appended
    Adds a new node to the end of the list
    Time Complexity : O(1) as the number of operations performed 
                      to add the new node at the end is always the same
    Steps:
        1. Point tail.next to the new node
        2. Set the tail to the new node.
    '''
    def append(self, value: any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    '''
    Removes the last Node from the linked list and returns it
    Time Complexity: O(n) as the entire linked list must be traversed to 
                     delete the last row and modify the tail
    Steps:
        1. Traverse the linked list to find the penultimate node.
        2. When the penultimate node is found modify it to be the tail and return the last node.
    '''
    def pop(self) -> any:
        if self.length == 0:
            return None
        elif self.length == 1:
            curr_node = self.head
            self.head   = None
            self.tail   = None
            self.length = 0
            return curr_node
        else:
            temp_node = self.head
            pre       = self.head
            while temp_node.next is not None:
                pre       = temp_node
                temp_node = temp_node.next
            self.tail      = pre
            self.tail.next = None
            self.length   -= 1
            return temp_node

    '''
    Adds a new node to the beginning of the list
    Time Complexity: O(1) as the number of operations being performed will
                     remain constant while adding a new node at the beginning
    Steps:
        1. If the list is empty set the new node as the head and tail of the list
        2. Set new_node.next = head
        3. Set head as new_node
    '''
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0 or self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True




my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.traverse()
item = my_ll.pop()
while item is not None:
    print(f'Value popped is: {item.value}')
    print('Linked list after pop operation: ', end="")
    my_ll.traverse()

    item = my_ll.pop()
print('Linked list is now empty')
my_ll.prepend(1)
my_ll.traverse()
my_ll.prepend(0)
my_ll.traverse()
my_ll.prepend(-1)
my_ll.traverse()
my_ll.append(2)
my_ll.traverse()