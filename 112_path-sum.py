# Problem Title: Path Sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

