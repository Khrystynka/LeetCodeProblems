# Problem Title: Relative Ranks
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_sorted = sorted(nums, reverse=True)
        d = {}
        for i in range(len(nums_sorted)):
            if i == 0:
                d[nums_sorted[i]] = 'Gold Medal'
            elif i == 1:
                d[nums_sorted[i]] = 'Silver Medal'
            elif i == 2:
                d[nums_sorted[i]] = 'Bronze Medal'
            else:
                d[nums_sorted[i]] = str(i+1)
        return [d[x] for x in nums]

