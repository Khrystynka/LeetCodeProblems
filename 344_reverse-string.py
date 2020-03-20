# Problem Title: Reverse String
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n > 1:
            for i in range(0, n/2):
                s[i], s[n-i-1] = s[n-i-1], s[i]

