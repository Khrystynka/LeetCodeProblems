# Problem Title: Inorder Successor in BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        found_node = False
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if found_node:
                return root
            if root == p:
                found_node = True
            root = root.right

