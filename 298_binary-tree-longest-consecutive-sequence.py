# Problem Title: Binary Tree Longest Consecutive Sequence
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxval = 0
        if not root:
            return 0

        def longest(node, prev_node_val, path_length=1):
            if node.val - 1 == prev_node_val:
                path_length += 1
            else:
                self.maxval = max(self.maxval, path_length)
                path_length = 1

            if node.right:
                longest(node.right, node.val, path_length)
            if node.left:
                longest(node.left, node.val, path_length)
            self.maxval = max(self.maxval, path_length)

        longest(root, None)
        return self.maxval

