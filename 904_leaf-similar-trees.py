# Problem Title: Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.res1 = []
        self.res2 = []

        def dfs(node, res):
            if node:
                if (node.left == None and node.right == None):
                    res.append(node.val)

                dfs(node.left, res)
                dfs(node.right, res)
            return res
        print dfs(root1, self.res1)
        print dfs(root2, self.res2)
        return self.res1 == self.res2

