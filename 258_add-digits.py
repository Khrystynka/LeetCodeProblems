# Problem Title: Add Digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num
        while res/10 != 0:
            suma = 0
            while res != 0:
                suma += res % 10
                res = res/10
            res = suma
        return res

