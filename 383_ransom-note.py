# Problem Title: Ransom Note
from collections import defaultdict


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(lambda: 0)
        for char in magazine:
            d[char] += 1
        for char in ransomNote:
            if d[char] == 0:
                return False
            else:
                d[char] -= 1
        return True

