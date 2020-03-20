# Problem Title: Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = 0
        n = len(s)
        i = 0
        while i < n:
            if (i+1) < n and d[s[i]] < d[s[i+1]]:
                num += d[s[i:i+2]]  # if s[i:i+2] in d else 0
                i = i+2
            else:
                num += d[s[i]]
                i = i+1
            # print num
        return num

