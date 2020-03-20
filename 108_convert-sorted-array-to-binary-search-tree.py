# Problem Title: Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)

        def build(start, end):
            if start > end or end >= n:
                return None

            root_idx = (start+end)/2
            root = TreeNode(nums[root_idx])
            root.left = build(start, root_idx-1)
            root.right = build(root_idx+1, end)
            return root
        return build(0, n-1)

