# Problem Title: Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def inord(node):
            if node:
                inord(node.left)
                res.append(node.val)
                inord(node.right)

        inord(root)
        return res

