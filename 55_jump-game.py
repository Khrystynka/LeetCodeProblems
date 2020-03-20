# Problem Title: Jump Game
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last_good_pos = n-1
        for i in range(n-2, -1, -1):
            if nums[i] >= last_good_pos-i:
                last_good_pos = i
        return last_good_pos == 0

