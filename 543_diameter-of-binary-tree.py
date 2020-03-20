# Problem Title: Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest_path = 0
        self.current_path = 0

        def path(node):
            if node == None:
                return 0
            right_depth = path(node.right)
            left_depth = path(node.left)
            self.current_path = right_depth+left_depth
            if self.current_path > self.longest_path:
                self.longest_path = self.current_path
            return max(right_depth, left_depth)+1
        depth = path(root)
        return self.longest_path

