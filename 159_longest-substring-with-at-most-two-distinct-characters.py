# Problem Title: Longest Substring with At Most Two Distinct Characters
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1 = 0
        p2 = 0
        max_len = 0
        n = len(s)
        d = {}
        l = 0
        while p2 < n:
            if len(d) < 3:
                d[s[p2]] = p2
                p2 += 1
            if len(d) == 3:
                # print d
                p1 = min(d.values())
                del d[(s[p1])]
                p1 += 1
            max_len = max(max_len, p2-p1)

        return max_len

