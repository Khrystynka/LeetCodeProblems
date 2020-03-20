# Problem Title: Construct Binary Tree from Inorder and Postorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        pos = {}
        for i, l in enumerate(inorder):
            pos[l] = i

        def SubTree(il, ir, pl, pr):
            if il > ir or pl > pr or ir < 0 or pr < 0:
                return None
            node = TreeNode(postorder[pr])
            pivot = pos[postorder[pr]]
            node.left = SubTree(il, pivot-1, pl, pl+(pivot-il)-1)
            node.right = SubTree(pivot+1, ir, pl+(pivot-il), pr-1)
            return node
        return SubTree(0, len(inorder)-1, 0, len(postorder)-1)

