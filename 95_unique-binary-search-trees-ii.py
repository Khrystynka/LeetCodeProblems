# Problem Title: Unique Binary Search Trees II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            res = []
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            for i in range(start, end+1):
                possibleLeftNodes = generate(start, i-1)
                possibleRightNodes = generate(i+1, end)
                # print 'left',possibleLeftNodes,'right',possibleRightNodes
                for l in possibleLeftNodes:
                    for r in possibleRightNodes:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        if n == 0:
            return []
        return generate(1, n)
        # print [l.val for l in res]

