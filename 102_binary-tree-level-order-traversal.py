# Problem Title: Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]

        def next_level(prev_level):
            new_level = []
            res_level = []
            for node in prev_level:
                if node.left:
                    new_level.append(node.left)
                    res_level.append(node.left.val)
                if node.right:
                    new_level.append(node.right)
                    res_level.append(node.right.val)
            if res_level == []:
                return
            res.append(res_level)
            next_level(new_level)
        next_level([root])
        return res

