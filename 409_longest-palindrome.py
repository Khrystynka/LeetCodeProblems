# Problem Title: Longest Palindrome
from collections import defaultdict


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        res = 0
        for el in s:
            d[el] += 1
        for k in d.keys():
            res += d[k]/2
        res = 2*res
        if len(s) > res:
            res += 1
        return res

