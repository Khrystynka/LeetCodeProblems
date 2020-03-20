# Problem Title: Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        """
        n is a power of three only if n in base 3 representation has only one 1:
        1,10,100...
        :type n: int
        :rtype: bool
        """
        base = 3
        res = 0
        if n <= 0:
            return False
        while n != 0:
            res += (n % base)
            n = n/base
        return (res) == 1

