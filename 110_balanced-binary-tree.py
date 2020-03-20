# Problem Title: Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.valid = True

        def isbalanced_height(node, h_sofar):
            if not node:
                return (True, h_sofar-1)
            left_balanced, height_left = isbalanced_height(
                node.left, 1+h_sofar)
            right_balanced, height_right = isbalanced_height(
                node.right, 1+h_sofar)
            if not left_balanced or not right_balanced:
                return (False, 0)
            return (abs(height_left - height_right) <= 1, max(height_left, height_right))
        return isbalanced_height(root, 0)[0]

