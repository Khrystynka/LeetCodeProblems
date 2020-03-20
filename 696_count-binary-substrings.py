# Problem Title: Count Binary Substrings
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prev = -1
        count1 = 0
        count0 = 0
        for i in range(len(s)):
            if s[i] == '0':
                if prev == '1':
                    res += min(count0, count1)
                    count0 = 1
                else:
                    count0 += 1
                prev = '0'

            else:
                if prev == '0':
                    res += min(count0, count1)
                    count1 = 1
                else:
                    count1 += 1
                prev = '1'

        res += min(count0, count1)
        return res

