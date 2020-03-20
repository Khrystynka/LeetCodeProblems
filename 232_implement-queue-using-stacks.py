# Problem Title: Implement Queue using Stacks
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyStack(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if not self.head:
            return None
        self.size -= 1
        res = self.head.val
        self.head = self.head.next
        return res

    def peek(self):
        if not self.head:
            return None
        return self.head.val

    def isempty(self):
        return self.size == 0


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2.isempty():
            while not self.stack1.isempty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2.isempty():
            while not self.stack1.isempty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1.isempty() and self.stack2.isempty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

