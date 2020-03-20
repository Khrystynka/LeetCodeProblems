# Problem Title: House Robber II
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def calc_dp(arr):
            if len(arr) <= 2:
                return max(arr)
            res = [0]*len(arr)
            res[0] = arr[0]
            res[1] = arr[1]
            res[2] = arr[2]+arr[0]
            for i in range(3, len(arr)):
                res[i] = max(res[i-2], res[i-3])+arr[i]
            return max(res)
        dp1 = calc_dp(nums[:-1])
        dp2 = calc_dp(nums[1:])
        return max(dp1, dp2)

