# Problem Title: Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head
        transform = {}
        node = head
        while node:
            if node not in transform:
                transform[node] = Node(node.val)
            new_node = transform[node]
            if node.next:
                if node.next not in transform:
                    transform[node.next] = Node(node.next.val)
                new_node.next = transform[node.next]
            if node.random:
                if node.random not in transform:
                    transform[node.random] = Node(node.random.val)
                new_node.random = transform[node.random]
            node = node.next
        return transform[head]

