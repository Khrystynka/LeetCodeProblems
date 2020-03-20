# Problem Title: Sort Colors
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums)-1
        i = 0
        while p2 >= i:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 = p2-1
            elif nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 = p1+1
                i += 1
            else:
                i = i+1

