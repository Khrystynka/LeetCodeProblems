# Problem Title: Assign Cookies
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        n = len(g)
        m = len(s)
        res = 0
        i = 0
        j = 0
        while i < n and j < m:
            while i < n and g[i] > s[j]:
                i += 1
            if i < n and g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
        return res

