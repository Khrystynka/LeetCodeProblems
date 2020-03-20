# Problem Title: Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return []
        level = [(root, str(root.val))]
        node = root
        while level != []:
            new_level = []
            for (node, path) in level:
                if not node.left and not node.right:
                    res.append(path)
                else:
                    if node.left:
                        new_level.append(
                            (node.left, path+'->'+str(node.left.val)))
                    if node.right:
                        new_level.append(
                            (node.right, path+'->'+str(node.right.val)))
                level = new_level
        return res

