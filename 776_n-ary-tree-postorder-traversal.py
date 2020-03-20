# Problem Title: N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.lst = []

        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                self.lst.append(node.val)
        traverse(root)
        return self.lst

