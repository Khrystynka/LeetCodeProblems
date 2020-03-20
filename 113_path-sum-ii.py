# Problem Title: Path Sum II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        def dfs(path=[], node=root, suma=sum):
            suma -= node.val
            if not node.right and not node.left:
                if suma == 0:
                    res.append(path+[node])
            if node.left:
                dfs(path+[node], node.left, suma)
            if node.right:
                dfs(path+[node], node.right, suma)
        dfs()
        return [[x.val for x in y] for y in res]

