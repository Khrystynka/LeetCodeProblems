# Problem Title: Valid Anagram
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = defaultdict(lambda: 0)
        for el in s:
            d[el] += 1
        for el in t:
            if d[el] == 0:
                return False
            d[el] -= 1
        return True

