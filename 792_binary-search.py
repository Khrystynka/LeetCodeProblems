# Problem Title: Binary Search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """  # [-1,0,3,5,9,12]
        mid_prev = -1
        left = 0
        right = len(nums)-1
        mid = left+(right-left)/2
        print left, right, mid
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            mid = left+(right-left)/2
            print left, right, mid
        return -1

