# Problem Title: Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        if len(nums) < k:
            return None
        val = sum(nums[:k])
        max_val = val
        for i in range(k, len(nums)):

            val = val+nums[i]-nums[i-k]
            if val > max_val:
                max_val = val
        return 1.0*max_val/k

