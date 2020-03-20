# Problem Title: Average of Levels in Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        res = []
        if root == None:
            return res
        curr_level, prev_level = 0, 0
        queu = [(root, curr_level)]
        sumval = 0
        count = 0
        while queu:
            (node, curr_level) = queu.pop(0)
            if node.left:
                queu.append((node.left, curr_level+1))
            if node.right:
                queu.append((node.right, curr_level+1))

            if curr_level != prev_level:
                res.append(1.0*sumval/count)
                sumval = 0
                prev_level = curr_level
                count = 0

            sumval += node.val
            count += 1
        res.append(1.0*sumval/count)

        return res

