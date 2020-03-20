# Problem Title: Reverse Words in a String II
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse(i, j):
            n = j-i
            for k in range(n/2):
                s[i+k], s[n+i-k-1] = s[n+i-k-1], s[i+k]
        reverse(0, len(s))
        p1 = 0
        p2 = 0
        while p2 < len(s):
            while p2 < len(s) and s[p2] != ' ':
                p2 += 1
            reverse(p1, p2)  # if p2<len(s)-1 else reverse(p1,p2+1)
            p1 = p2+1
            p2 = p1

