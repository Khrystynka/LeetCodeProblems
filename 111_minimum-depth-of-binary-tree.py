# Problem Title: Minimum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_depth = float('inf')
        if not root:
            return 0

        def mindepth(node, depth):
            if node:

                if depth >= self.min_depth:
                    return self.min_depth
                if not node.left and not node.right:
                    self.min_depth = min(depth, self.min_depth)
                    return self.min_depth
                return min(self.min_depth, mindepth(node.left, depth+1), mindepth(node.right, depth+1))
            else:
                return self.min_depth
        return mindepth(root, 1)

