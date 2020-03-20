# Problem Title: Two Sum IV - Input is a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = {}

        def inorder(node, k):
            if node == None:
                return False
            if node.val in res:
                return True
            else:
                res[k-node.val] = 1

            return inorder(node.left, k) or inorder(node.right, k)
        return inorder(root, k)

