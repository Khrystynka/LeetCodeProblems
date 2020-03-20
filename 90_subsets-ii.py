# Problem Title: Subsets II
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        prev_len = 0
        start = 0
        res = [[]]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                start = prev_len
            else:
                start = 0
            prev_len = len(res)
            print nums[i], start, res[start:]
            for j in res[start:]:

                res.append(j+[nums[i]])
        return res

