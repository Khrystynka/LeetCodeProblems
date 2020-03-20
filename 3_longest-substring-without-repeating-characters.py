# Problem Title: Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = dict()
        start = 0
        n = len(s)
        max_len = 0
        for end in range(0, n):
            if s[end] not in seen or seen[s[end]] < start:
                max_len = max(max_len, end-start+1)

            else:
                start = max(seen[s[end]]+1, start)
            seen[s[end]] = end

        return max_len

