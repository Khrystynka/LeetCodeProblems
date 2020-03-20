# Problem Title: Min Stack
class Node(object):
    def __init__(self, val=None):
        self.value = val
        self.next = None


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = None
        self.min_stack = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        new_node = Node(x)
        new_node.next = self.stack
        self.stack = new_node

        if (self.min_stack and self.min_stack.value >= x) or self.min_stack == None:
            new_min_node = Node(x)
            new_min_node.next = self.min_stack
            self.min_stack = new_min_node

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.value == self.min_stack.value:
            self.min_stack = self.min_stack.next
        self.stack = self.stack.next

    def top(self):
        """
        :rtype: int
        """
        return self.stack.value

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack.value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

