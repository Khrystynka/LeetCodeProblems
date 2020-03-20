# Problem Title: Implement strStr()
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if needle == '':
            return 0

        if n < m or n == 0:
            return -1

        pointer = 0
        while pointer <= n-m:
            j = 0
            if haystack[pointer] == needle[j]:
                i = pointer+1
                j = j+1
                while j < m and i < n and haystack[i] == needle[j]:
                    i = i+1
                    j = j+1
                if j == m:
                    return pointer
                if i >= n:
                    return -1

            pointer = pointer+1
        return -1

