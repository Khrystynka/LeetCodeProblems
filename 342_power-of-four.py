# Problem Title: Power of Four
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = 0
        if num <= 0:
            return False
        while num != 0:
            res += num % 4
            num = num/4
        return res == 1

