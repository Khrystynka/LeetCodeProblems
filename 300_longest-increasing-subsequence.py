# Problem Title: Longest Increasing Subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            res = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dp[j]+1)
            dp[i] = res
        return max(dp)

