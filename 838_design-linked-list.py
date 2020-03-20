# Problem Title: Design Linked List
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if 0 > index or index >= self.size or not self.head:
            return -1
        node = self.head
        i = 0
        while i < index:
            node = node.next
            i += 1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if index > self.size:
            return
        if self.head == None:
            self.head = new_node

        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            i = 0
            node = self.head
            while i < index-1:
                node = node.next
                i = i+1
            new_node.next = node.next
            node.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            if self.head:
                self.head = self.head.next
                self.size -= 1
            else:
                return
        elif 0 < index < self.size:
            i = 0
            node = self.head
            while i < index-1:
                node = node.next
                i += 1
            node.next = node.next.next
            self.size -= 1

