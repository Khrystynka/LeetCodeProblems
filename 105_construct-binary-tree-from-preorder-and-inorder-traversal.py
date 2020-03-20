# Problem Title: Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inord_dict = {}
        for i in range(len(inorder)):
            inord_dict[inorder[i]] = i
        n = len(preorder)
        if n != len(inorder) or n == 0:
            return None

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start >= n or in_start >= n or pre_end >= n or in_end >= n or pre_start > pre_end or in_start > in_end:
                return None
            root = TreeNode(preorder[pre_start])
            root_ind = inord_dict[preorder[pre_start]]
            root.left = build(pre_start+1, pre_start +
                              root_ind-in_start, in_start, root_ind)
            root.right = build(pre_start+1+root_ind-in_start,
                               pre_end, root_ind+1, in_end)
            return root

        return build(0, n-1, 0, n-1)

