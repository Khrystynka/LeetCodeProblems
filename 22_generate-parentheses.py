# Problem Title: Generate Parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []

        def helper(opened, closed, s=''):
            if opened == n and closed == n:
                self.res.append(s)
                return
            if opened < closed or closed > n or opened > n:
                return

            helper(opened+1, closed, s+'(')
            helper(opened, closed+1, s+')')
        helper(0, 0, '')
        return self.res

