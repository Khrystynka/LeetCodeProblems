# Problem Title: Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# recursive solution
'''class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def depth(node):
            if node == None: return 0
            return  max(depth(child) for child in node.children)+1 if node.children else 1
        return depth(root)'''

# bfs
'''class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        level=1
        queu=[(root,level)]

        while queu:
            tup= queu.pop(0)
            node= tup[0]
            if node.children!=[]:
                level=tup[1]+1
                for child in node.children:
                    queu.append((child,level))
        return level
        '''
# dfs


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        max_depth = 1
        depth = 1
        stack = [(root, depth)]
        while stack:
            (node, depth) = stack.pop()
            if node.children != []:
                depth = depth+1
                for child in node.children:
                    stack.append((child, depth))
            else:
                max_depth = max(depth, max_depth)
        return max_depth

