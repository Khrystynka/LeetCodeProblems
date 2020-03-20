# Problem Title: Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        strs = sorted(strs)
        first_w = strs[0]
        last_w = strs[-1]
        if first_w > last_w:
            prefix = last_w
            word = first_w
        else:
            prefix = first_w
            word = last_w
        while word[:len(prefix)] != prefix and len(prefix) > 0:
            prefix = prefix[:-1]
            # print prefix
        return prefix

