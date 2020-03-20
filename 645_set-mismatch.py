# Problem Title: Set Mismatch
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for el in nums:
            if el in d:
                res.append(el)
                d[el] += 1
            else:
                d[el] = 1
        for el in range(1, len(nums)+1):
            if el not in d:
                res.append(el)
                return res

