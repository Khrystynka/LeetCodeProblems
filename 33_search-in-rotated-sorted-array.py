# Problem Title: Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        pivot_ind = -1
        if n == 0:
            return -1
        if nums[n-1] > nums[0]:
            pivot_ind = n-1
        while left <= right:
            mid = left+(right-left+1)/2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if mid < n-1 and nums[mid] >= nums[mid+1]:
                    pivot_ind = mid
                    break
                else:
                    left = mid+1
            else:
                right = mid-1
        left = 0 if target >= nums[0] else pivot_ind
        right = pivot_ind if target >= nums[0] else n-1
        while left <= right:
            mid = left+(right-left+1)/2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

