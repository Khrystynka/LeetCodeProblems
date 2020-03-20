# Problem Title: Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        for i, el in enumerate(nums):
            if target-el in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target-el)]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

