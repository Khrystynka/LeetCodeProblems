# Problem Title: Flip Game II
class Solution(object):
    memo = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.memo:
            return self.memo[s]
        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                if not self.canWin(s[:i-1]+'--'+s[i+1:]):
                    self.memo[s] = True
                    return True
        self.memo[s] = False
        return False

