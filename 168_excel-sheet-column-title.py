# Problem Title: Excel Sheet Column Title
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        rest = n
        while rest > 26:
            last = rest % 26
            if last != 0:
                s = s+chr(64+last)
            else:
                s = s+chr(64+26)
                rest = rest-26
            rest = rest/26
        s = s+chr(64+rest)
        return s[::-1]

