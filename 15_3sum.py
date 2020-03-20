# Problem Title: 3Sum
class Solution(object):
    def threeSum(self, nums):
        res = set()
        n = len(nums)

        if n < 3:
            return []
        if nums.count(0) >= 3:
            res.add((0, 0, 0))
        nums.sort()
        if nums[-1] <= 0:
            return res
        for i in range(n-2):
            end = n-1
            if nums[i] >= 0:
                return res
            for j in range(i+1, n-1):
                k = -nums[i]-nums[j]
                if k <= nums[end]:
                    while end >= j+1 and k < nums[end]:
                        end -= 1
                    if end >= j+1 and k == nums[end]:
                        res.add((nums[i], nums[j], nums[end]))
        return res

