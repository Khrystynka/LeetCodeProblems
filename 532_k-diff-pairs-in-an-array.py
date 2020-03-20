# Problem Title: K-diff Pairs in an Array

class Solution:
    def findPairs(self, nums, k):
        res = 0
        d = {}
        nums_unique = set(nums)
        if k == 0:
            for el in nums:
                if el in d.keys():
                    d[el] += 1
                else:
                    d[el] = 1
            for k in d.keys():
                if d[k] > 1:
                    res += 1
        if k > 0:
            for el in nums_unique:
                if k+el in nums_unique:
                    res += 1
        return res

