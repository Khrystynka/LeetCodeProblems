# Problem Title: Reverse Integer
import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = ''
        neg = False
        if x < 0:
            neg = True
            x = x*(-1)
        s = str(x)
        res = s[::-1]
        res = int(res)
        if (not neg and res > 2**31) or (neg and -res < (-2**31-1)):
            return 0
        else:
            return -res if neg else res

