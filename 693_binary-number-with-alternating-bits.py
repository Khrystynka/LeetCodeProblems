# Problem Title: Binary Number with Alternating Bits
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1
        n = n >> 1
        while n:
            last = n & 1
            n = n >> 1
            if last == prev:
                return False
            prev = last
        return True

