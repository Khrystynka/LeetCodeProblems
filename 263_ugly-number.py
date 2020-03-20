# Problem Title: Ugly Number
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def max_div(x, y):
            if x == 0:
                return x
            while x % y == 0:
                x = x/y
            return x
        num = max_div(num, 5)
        num = max_div(num, 3)
        num = max_div(num, 2)

        return num == 1

