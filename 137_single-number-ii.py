# Problem Title: Single Number II
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        indiv = set(nums)
        for num in indiv:
            res += 3*num
        return (res-sum(nums))/2

