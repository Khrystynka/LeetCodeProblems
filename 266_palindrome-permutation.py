# Problem Title: Palindrome Permutation
from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = defaultdict(lambda: 0)
        count_odd = 0
        for char in s:
            d[char] += 1
            if d[char] % 2 != 0:
                count_odd += 1
            else:
                count_odd -= 1
        return count_odd <= 1

