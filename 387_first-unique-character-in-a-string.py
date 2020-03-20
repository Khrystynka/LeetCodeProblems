# Problem Title: First Unique Character in a String
from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        for char in s:
            d[char] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

