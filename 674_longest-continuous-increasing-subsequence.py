# Problem Title: Longest Continuous Increasing Subsequence
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        cur_len = 1
        max_len = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1
        return max(max_len, cur_len)

