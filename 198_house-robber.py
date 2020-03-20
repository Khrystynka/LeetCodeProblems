# Problem Title: House Robber
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_profit = 0
        second_profit = 0
        curr_profit = 0
        for i in range(len(nums)):
            curr_profit = max(first_profit+nums[i], second_profit)
            first_profit = second_profit
            second_profit = curr_profit
        return curr_profit

