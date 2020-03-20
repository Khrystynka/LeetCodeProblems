# Problem Title: Sum of Left Leaves
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = [root]
        left_leaves = []
        while stack:
            next = stack.pop()
            left_child = next.left
            right_child = next.right
            if left_child != None:
                stack.append(left_child)
            if right_child != None:

                stack.append(right_child)
            if left_child and left_child.left == None and left_child.right == None:
                left_leaves.append(left_child)
        return sum(map(lambda x: x.val, left_leaves))

