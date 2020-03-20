# Problem Title: Find Peak Element
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)/2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == n-1 and nums[mid] > nums[mid-1]) or (mid != 0 and mid != n-1 and nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
                return mid
            elif nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid-1

