# Problem Title: Second Minimum Node In a Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.first_min = root.val
        self.second_min = float('inf')

        def dfs(node):
            if node:
                if self.first_min < node.val < self.second_min:
                    self.second_min = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.second_min if self.second_min < float('inf') else -1

