# Problem Title: Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        n = len(s)
        for i in range(0, n):
            number = number*26+(ord(s[i])-64)
        return number

