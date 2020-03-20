# Problem Title: Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        prev1 = 0
        prev2 = 1
        for i in range(n):
            res = prev1+prev2
            prev1 = prev2
            prev2 = res
        return res

