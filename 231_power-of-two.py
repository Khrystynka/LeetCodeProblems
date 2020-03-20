# Problem Title: Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        bit_count = 0
        while n:
            bit_count += n & 1
            n = n >> 1
        return bit_count == 1

