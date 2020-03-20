# Problem Title: 3Sum Closest
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        nums = sorted(nums)
        diff = float('inf')
        res = 0
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = n-1
            while start < end:
                suma = nums[i]+nums[start]+nums[end]

                if (target-suma) == 0:
                    return suma
                if abs(target-suma) < diff:
                    diff = abs(target-suma)
                    res = suma
                if suma < target:
                    while start < n-1 and nums[start] == nums[start+1]:
                        start += 1
                    start += 1
                else:
                    while end > 1 and nums[end] == nums[end-1]:
                        end -= 1
                    end = end-1

        return res

