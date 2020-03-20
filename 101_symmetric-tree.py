# Problem Title: Symmetric Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def equal(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if (tree1 and not tree2) or (tree2 and not tree1):
                return False
            return tree1.val == tree2.val and equal(tree1.left, tree2.right) and equal(tree1.right, tree2.left)
        if not root:
            return True
        return equal(root.left, root.right)

