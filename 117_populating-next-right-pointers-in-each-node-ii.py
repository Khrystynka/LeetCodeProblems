# Problem Title: Populating Next Right Pointers in Each Node II
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
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
            return root

        def makeconnection(node, parent_node, left=True):
            if not left and not parent_node.next:
                return
            if left and parent_node.right:
                node.next = parent_node.right
                makeconnection(parent_node.right, parent_node, False)
                return
            while parent_node.next:
                parent_node = parent_node.next
                if parent_node.left:
                    node.next = parent_node.left
                    makeconnection(parent_node.left, parent_node, True)
                    return
                if parent_node.right:
                    node.next = parent_node.right
                    makeconnection(parent_node.right, parent_node, False)
                    return

        startnode = root

        while 1:
            if not startnode.left and not startnode.right and not startnode.next:
                return root
            if startnode.left:
                makeconnection(startnode.left, startnode, True)
                startnode = startnode.left
            elif startnode.right:
                makeconnection(startnode.right, startnode, False)
                startnode = startnode.right
            else:
                startnode = startnode.next
        return root

