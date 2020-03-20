# Problem Title: Populating Next Right Pointers in Each Node
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        root.next = None

        def bfs(first_node):  # first node- first node from previous level
            if not first_node.left:
                return
            temp = first_node.left
            right_node = None
            while first_node:
                if right_node:
                    right_node.next = first_node.left
                first_node.left.next = first_node.right
                right_node = first_node.right
                first_node = first_node.next
            # print right_node.val

            right_node.next = None

            bfs(temp)
        bfs(root)
        return root

