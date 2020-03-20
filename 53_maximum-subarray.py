# Problem Title: Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = 0
        for el in nums:
            curr_sum = max(el, curr_sum+el)
            max_sum = max(max_sum, curr_sum)
        return max_sum

