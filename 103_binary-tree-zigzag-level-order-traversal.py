# Problem Title: Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]

        def nextlevel(prev_level, forward=False):
            level = []
            for node in prev_level:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level == []:
                return
            if forward:
                res.append([x.val for x in level])
            else:
                res.append([x.val for x in level[::-1]])
            nextlevel(level, not forward)
        nextlevel([root])
        return res

