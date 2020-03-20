# Problem Title: 4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n-3):
            if i == 0 or nums[i] > nums[i-1]:
                for j in range(i+1, n-2):
                    if j == i+1 or nums[j] > nums[j-1]:
                        start = j+1
                        end = n-1
                        while start < end:
                            if nums[i]+nums[j]+nums[start]+nums[end] == target:
                                res.append(
                                    [nums[i], nums[j], nums[start], nums[end]])
                            if nums[i]+nums[j]+nums[start]+nums[end] < target:
                                prev_start = start
                                while start < n and nums[start] == nums[prev_start]:
                                    prev_start = start
                                    start += 1
                            else:
                                prev_end = end
                                while end > j and nums[end] == nums[prev_end]:
                                    prev_end = end
                                    end -= 1
        return res

