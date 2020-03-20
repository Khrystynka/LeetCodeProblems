# Problem Title: Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        count = 1
        prev = nums[0]
        p1 = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if count < 2:
                    count += 1
                    nums[p1] = nums[i]
                    p1 = p1+1
            else:
                count = 1
                nums[p1] = nums[i]
                p1 = p1+1
        return p1

