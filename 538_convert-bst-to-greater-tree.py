# Problem Title: Convert BST to Greater Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''class Solution(object):
    def convertBST(self, root):
        # reversed in order traversal (right-root-left) in BST leads to reversed #sorted array
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum_sofar=0
        def reversedInOrder(node):
            if node:
                reversedInOrder(node.right)
                node.val=node.val+self.sum_sofar
                self.sum_sofar=node.val
                reversedInOrder(node.left)
        reversedInOrder(root)
        return root'''
# Non recursive solution


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        total = 0
        stack = [root]
        node = root.right
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root

