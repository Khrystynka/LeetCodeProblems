# Problem Title: Paint Fence
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        same = 0
        diff = k
        for i in range(n-1):
            same_prev = same
            diff_prev = diff
            same = diff_prev
            diff = (same_prev+diff_prev)*(k-1)
        return same+diff

