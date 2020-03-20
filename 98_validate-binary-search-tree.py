# Problem Title: Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, upper_limit, lower_limit):
            if not node:
                return True
            if (upper_limit != None and node.val >= upper_limit) or (lower_limit != None and node.val <= lower_limit):
                return False
            # print 'node.left',node.left,'upper',node.val,'lower',lower_limit
            # print 'node.right',node.right,'upper',upper_limit,'lower',node.val
            return valid(node.left, node.val, lower_limit) and valid(node.right, upper_limit, node.val)

        return valid(root, None, None)

