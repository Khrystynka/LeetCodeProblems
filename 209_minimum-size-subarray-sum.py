# Problem Title: Minimum Size Subarray Sum
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        p1 = 0
        min_len = float('inf')
        p2 = 0
        curr_sum = nums[p1]
        while p2 < n:
            if curr_sum >= s:
                min_len = min(min_len, p2-p1+1)
                curr_sum -= nums[p1]
                p1 = p1+1
            elif p2 < n-1:
                p2 += 1
                curr_sum += nums[p2]
            else:
                return 0 if min_len == float('inf') else min_len

