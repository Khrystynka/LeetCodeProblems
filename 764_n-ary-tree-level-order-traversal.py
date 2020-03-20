# Problem Title: N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queu = [root]
        next_level = []
        res = [[root.val]]
        while True:
            while queu:
                node = queu.pop(0)
                for child in node.children:
                    next_level.append(child)
            if next_level == []:
                return res
            res.append([child.val for child in next_level])
            queu = (next_level)
            next_level = []
        return res

