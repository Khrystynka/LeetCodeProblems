# Problem Title: Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1:
            return 1
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        res = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return res*res
        else:
            return x*res*res

