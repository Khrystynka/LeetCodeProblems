# Problem Title: Minimum Distance Between BST Nodes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_min = float('inf')
        self.inord = []

        def inorder(node):
            if node:

                inorder(node.left)
                self.inord.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in range(1, len(self.inord)):
            if (self.inord[i]-self.inord[i-1]) < curr_min:
                curr_min = self.inord[i]-self.inord[i-1]
        return curr_min

