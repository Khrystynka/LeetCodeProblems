# Problem Title: Summary Ranges
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        res = []
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1]+1:
                res.append(str(nums[start])+'->'+str(nums[i-1])
                           if (i-1) != start else str(nums[start]))
                start = i
        return res

