# Problem Title: Valid Perfect Square
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = 0
        i = 1
        while res < num:
            res += i
            i += 2
        if res == num:
            return True
        else:
            return False

