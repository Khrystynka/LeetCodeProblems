# Problem Title: Find Minimum in Rotated Sorted Array
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        if right == 0:
            return nums[0]
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1

