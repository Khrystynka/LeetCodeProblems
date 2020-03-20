# Problem Title: Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        p = 0
        for i in range(n):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
        return p+1

