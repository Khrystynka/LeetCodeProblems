# Problem Title: Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return 0

        def dfs(num_sofar, node):
            if not node.left and not node.right:
                res.append(num_sofar+str(node.val))
                return
            if node.left:
                dfs(num_sofar+str(node.val), node.left)
            if node.right:
                dfs(num_sofar+str(node.val), node.right)
        dfs('', root)
        # print res
        return sum(map(int, res))

