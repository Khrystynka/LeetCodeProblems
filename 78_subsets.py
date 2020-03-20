# Problem Title: Subsets
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            for j in res[:]:
                # print j
                res.append(j+[i])
        return res

