# Problem Title: Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depthleft = self.maxDepth(root.left)
        depthright = self.maxDepth(root.right)
        return max(depthleft, depthright)+1

