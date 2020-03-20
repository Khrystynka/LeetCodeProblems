# Problem Title: Flatten Binary Tree to Linked List
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        right = root.right
        self.flatten(root.left)
        root.right = root.left
        root.left = None

        while root.right:
            root = root.right
        self.flatten(right)
        root.right = right

