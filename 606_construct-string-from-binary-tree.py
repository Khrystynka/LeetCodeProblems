# Problem Title: Construct String from Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # self.s=''
        def preorder(node):
            if not node:
                return ''
            if node.left == None and node.right == None:
                return str(node.val)
            if node.left and node.right == None:
                return str(node.val)+'('+preorder(node.left)+')'
            return str(node.val)+(('('+preorder(node.left)+')') if node.left else '()') + '('+preorder(node.right)+")"
        return preorder(t)

