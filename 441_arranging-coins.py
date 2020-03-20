# Problem Title: Arranging Coins
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fn(x):
            return (x**2+x)/2
        l = 0
        r = n
        mid = (r-l)/2
        f = fn(mid)
        while l <= r:
            if f == n:
                return mid
            elif f > n and fn(mid-1) <= n:
                return mid-1
            elif f < n:
                l = mid+1
            else:
                r = mid-1

            mid = l+(r-l)/2
            f = fn(mid)

        return (mid)

