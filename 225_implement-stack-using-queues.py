# Problem Title: Implement Stack using Queues
class Node(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class MyQueu(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_to_back(self, x):
        if not self.tail:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.size += 1

    def peek_from_front(self):
        if self.head:
            return self.head.val

    def pop_from_front(self):
        elem = None
        if self.head:
            elem = self.head.val
            self.head = self.head.next
            self.size -= 1

        if not self.head:
            self.tail = None
        return elem


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queu = MyQueu()
        self.top_el = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queu.push_to_back(x)
        self.top_el = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queu.size == 1:
            self.top_el = None
        for i in range(self.queu.size-1):
            self.top_el = self.queu.pop_from_front()
            self.queu.push_to_back(self.top_el)
        return self.queu.pop_from_front()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_el

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return self.queu.size == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

