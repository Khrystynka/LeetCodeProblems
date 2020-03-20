# Problem Title: Missing Number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 1:
            return 1 - nums[0]
        expected_sum = n*(n+1)/2
        # print expected_sum

        return expected_sum-(sum(nums))

