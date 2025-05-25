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
    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0 or self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head     = new_node
        self.length += 1
        return True

    '''
    Removes the first node from the list and returns it
    Time Complexity: O(1) as the number of operations to remove the first node
                     from the list will always remain the same.
    Steps:
        1. If the list is empty return None
        2. If the list has only one node set the head and tail to None,
           decrement the length and return the node.
        3. Set the head to the next node, decrement the length and return
           the first node.
    '''
    def pop_first(self):
        if self.length == 0 or self.head is None:
            return None
        elif self.length == 1:
            temp = self.head
            self.head    = None
            self.tail    = None
            self.length -= 1
            temp.next    = None
            return temp
        temp         = self.head
        self.head    = self.head.next
        temp.next    = None
        self.length -= 1
        return temp

    '''
    Retrieves the node at the specified index.
    Time Complexity: o(n) as we would have to iterate over the list each time to
                     retrieve the node at the given index.
    Steps:
        1. If index is < 0 or index > length of the index return None
        2. Iterate over the list to retrieve the node at the given index
    '''
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    '''
    Sets the value of the node at the specified index with the given value.
    Time Complexity: O(n) as the number of operations performed depends on the index
                     at which the value is being set.
    Steps:
        1. If index < 0 or index >= length of the list, return None
        2. Loop over the lists till the node at given index is reached and set the value.  
    '''
    def set_value(self, index: int, value: any) -> any:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    '''
    Creates a new node with the given value at the specified index.
    Time Complexity: O(n) as the number of operations depends on the
                     index at which the new node is being inserted.
    Steps:
        1. Check if the index is valid. Return False if an invalid index is given.
        2. If the new node is being inserted at the head, use the prepend method.
        3. If the new node is being inserted at the tail, use the append method.
        4. Else retrieve the node at index - 1, point the new node to the existing nodes next.
        5. Point the existing node to the new node, increment the length by 1 and return True.
    '''
    def insert(self, index: int, value: any) -> bool:
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.prepend(value)
        else:
            new_node  = Node(value)
            temp_node = self.get(index - 1)
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
            return True

    '''
    Removes the node at the given index and returns it.
    Time Complexity: O(n) as the number of operations depends on the index from 
                     which the node is being removed.
    Steps:
        1. If the index < 0 or index >= self.length, return False
        2. If the index == 0, use the pop_first method to delete the head
        3. If the index == self.length - 1, use the pop method to delete the tail.
        4. Else retrieve the node at index - 1 and index.
        5. Point the node at index - 1 to index.next.
        6. Point the node at index to None
        7. Decrement the length and return the node
    '''
    def remove(self, index: int) -> any([Node, bool]):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index ==  self.length - 1:
            return self.pop()
        else:
            pre       = self.get(index - 1)
            curr      = pre.next
            pre.next  = curr.next
            curr.next = None
            self.length -= 1
            return curr

    def reverse(self):
        temp      = self.head
        self.head = self.tail
        self.tail = temp
        pre       = None
        after     = temp.next
        for _ in range(self.length):
            after     = temp.next
            temp.next = pre
            pre       = temp
            temp      = after

