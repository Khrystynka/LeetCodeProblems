# Problem Title: Binary Tree Tilt
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0
        def sum_val(node):

            (sum_left, sum_right) = (0, 0)
            if node == None:
                return 0
            if node.left:
                sum_left = sum_val(node.left)

            if node.right:
                sum_right = sum_val(node.right)
            res = abs(sum_left-sum_right)
            self.total += res
            return sum_left+sum_right+node.val
        sum_val(root)
        return self.total

