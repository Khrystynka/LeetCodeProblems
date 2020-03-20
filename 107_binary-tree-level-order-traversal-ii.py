# Problem Title: Binary Tree Level Order Traversal II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        prev_level = [root]
        while prev_level:
            res.append([x.val for x in prev_level])
            level = []
            for node in prev_level:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            prev_level = level
        return res[::-1]

