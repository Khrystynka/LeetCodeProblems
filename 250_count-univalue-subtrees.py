# Problem Title: Count Univalue Subtrees
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def isuni(node):
            if not node:
                return True
            isleft = isuni(node.left)
            isright = isuni(node.right)
            if (node.left == None or node.val == node.left.val) and (node.right == None or node.right.val == node.val) and isleft and isright:
                self.count += 1
                return True
        isuni(root)
        return self.count

