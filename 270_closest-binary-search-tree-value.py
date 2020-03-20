# Problem Title: Closest Binary Search Tree Value
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        def findclosest(root, target, closest):
            if not root:
                return closest
            if root.val == target:
                return root.val
            closest = min(root.val, closest, key=lambda x: abs(x-target))
            if root.val > target:
                return findclosest(root.left, target, closest)
            else:
                return findclosest(root.right, target, closest)
        return findclosest(root, target, float('inf'))

