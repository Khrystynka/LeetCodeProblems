# Problem Title: One Edit Distance
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n > m+1 or m > n+1:
            return False
        if n > m:
            s, t = t, s
            n, m = m, n
        if n == 0:
            return m == 1
        for i in range(n):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] if n == m else s[i:] == t[i+1:]
        return n != m

