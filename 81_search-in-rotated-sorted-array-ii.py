# Problem Title: Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binary_search(arr, target):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left+right)/2
                if arr[mid] == target:
                    return True
                if arr[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False

        if nums == []:
            return False
        n = len(nums)
        left = 0
        right = n-1
        max_el_ind = -1
        while nums[left] == nums[right] and left < right:
            right = right-1
        if nums[right] > nums[left]:
            return binary_search(nums[left:right+1], target)

        while left <= right:
            mid = (right+left)/2
            if mid < n-1 and nums[mid] > nums[mid+1]:
                max_el_ind = mid
                break
            if nums[mid] < nums[left]:
                right = mid-1
            else:
                left = mid+1
        if max_el_ind == -1:
            return target == nums[0]
        if target < nums[0]:
            return binary_search(nums[max_el_ind+1:], target)
        else:
            return binary_search(nums[:max_el_ind+1], target)

