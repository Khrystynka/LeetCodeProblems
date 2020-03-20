# Problem Title: Count Complete Tree Nodes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def finddepth(node):
            if not node:
                return -1
            depth = 0
            while node.left:
                depth += 1
                node = node.left
            return depth

        def existnode(root, depth, idx):
            left = 0
            right = (2**depth-1)
            for d in range(depth):
                middle = (right+left)/2
                if idx <= middle:
                    root = root.left
                    right = middle
                else:
                    root = root.right
                    left = middle+1
            return root != None

        def binsearch(root, depth):
            left = 0
            right = 2**depth-1
            while left <= right:
                mid = (right+left)/2
                if existnode(root, depth, mid):
                    left = mid+1
                else:
                    right = mid-1
            return left

        depth = finddepth(root)
        if depth == -1:
            return 0
        if depth == 0:
            return 1
        return 2**depth-1+binsearch(root, depth)

