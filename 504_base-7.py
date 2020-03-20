# Problem Title: Base 7
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        s = ''
        neg = False
        if num < 0:
            neg = True
            num = abs(num)
            print num
        while num != 0:
            s += str(num % 7)
            num = num/7

        return s[::-1] if not neg else '-'+s[::-1]

