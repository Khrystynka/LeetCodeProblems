# Problem Title: Binary Tree Upside Down
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def connect(root=root):
            if not root or not root.left:
                return root
            newroot = connect(root.left)
            # print newroot.val
            root.left.right = root
            root.left.left = root.right
            root.left = None
            root.right = None
            return newroot
        return connect()

