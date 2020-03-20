# Problem Title: Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxlen = 0
        res = ''
        for i in range(n):
            start = i-1
            end = i+1
            curr_len = 0
            while start >= 0 and end < n and s[start] == s[end]:
                curr_len += 2
                start -= 1
                end += 1
            if curr_len+1 > maxlen:
                res = s[start+1:end]
                maxlen = curr_len
            start = i
            end = i+1
            curr_len = 0
            while start >= 0 and end < n and s[start] == s[end]:
                curr_len += 2
                start -= 1
                end += 1
            if curr_len > maxlen:
                res = s[start+1:end]
                maxlen = curr_len
        return res

