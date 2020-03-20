# Problem Title: Group Shifted Strings
from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        res = []
        d = defaultdict(lambda: [])
        for string in strings:
            temp = []
            for i in range(len(string)-1):
                temp.append((ord(string[i+1])-ord(string[i])) % 26)
            d[tuple(temp)].append(string)
        return list(d.values())

