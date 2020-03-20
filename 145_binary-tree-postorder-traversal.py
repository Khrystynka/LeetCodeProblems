# Problem Title: Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''stack=[]
        res=[]
        node=root
        developed=set()
        while node or stack:
            #print [x.val for x in stack]
            while node:
                stack.append(node)
                node=node.left
            node=stack[-1]
            if node not in developed and node.right:
                developed.add(node)
                node=node.right
            else:
                node=stack.pop()
                res.append(node.val)
                node=None
        return res'''
        self.res = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            self.res.append(node.val)
        postorder(root)
        return self.res

