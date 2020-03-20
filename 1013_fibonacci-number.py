# Problem Title: Fibonacci Number
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {0: 0, 1: 1}
        for i in range(2, N+1):
            d[i] = d[i-2]+d[i-1]
        return d[N]

