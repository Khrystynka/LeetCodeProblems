# Problem Title: Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = 0
        for i in d:
            if i+1 in d:
                t = d[i] + d[i+1]
                if t > m:
                    m = t
        return m

