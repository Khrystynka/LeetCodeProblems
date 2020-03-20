# Problem Title: Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        quant = n/5
        while quant > 0:
            res += quant
            quant = quant/5
        return res

