# Problem Title: Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n not in d and n != 1:
            d.add(n)
            res = 0
            while n != 0:
                res += (n % 10)**2
                n = n/10
            n = res

        return n == 1

