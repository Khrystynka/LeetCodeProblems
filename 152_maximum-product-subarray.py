# Problem Title: Maximum Product Subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        extr1 = nums[0]
        extr2 = nums[0]
        total_max = nums[0]
        for num in nums[1:]:
            old_extr1 = extr1
            extr1 = max(num, extr1*num, extr2*num)
            extr2 = min(num, old_extr1*num, extr2*num)
            total_max = max(total_max, extr1, extr2)
        return total_max

