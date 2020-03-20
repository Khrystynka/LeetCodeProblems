# Problem Title: Find Mode in Binary Search Tree
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res, self.maxcount, self.curcount, self.curnum = [
        ], 0, 0, float("-Inf")

        def helper(node):
            if node:
                helper(node.left)
                if self.curnum != node.val:
                    self.curnum = node.val
                    self.curcount = 1
                else:
                    self.curcount += 1
                if self.curcount == self.maxcount:
                    self.res.append(node.val)
                elif self.curcount > self.maxcount:
                    self.maxcount = self.curcount
                    self.res = [node.val]
                helper(node.right)

        helper(root)
        return self.res

