# Problem Title: Minimum Absolute Difference in BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.curr_diff = float('Inf')
        self.prev_node = float('-Inf')
        self.min_diff = float('Inf')

        def inorder(node):
            if node:
                inorder(node.left)

                self.curr_diff = node.val-self.prev_node
                if self.curr_diff < self.min_diff:
                    self.min_diff = self.curr_diff
                self.prev_node = node.val

                inorder(node.right)
        inorder(root)
        return self.min_diff

