# Problem Title: Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                first = mid
                last = mid
                while first >= 1 and nums[first-1] == target:
                    first = first-1
                while last < n-1 and nums[last+1] == target:
                    last = last+1
                return [first, last]
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [-1, -1]

