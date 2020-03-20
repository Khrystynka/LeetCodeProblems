# Problem Title: Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum == total-curr_sum-nums[i]:
                return i
            curr_sum += nums[i]
        return -1

