# Problem Title: Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        n = len(nums)
        l_id = 0
        r_id = n-1

        while r_id < n and r_id >= 0 and l_id >= 0 and l_id < n and l_id <= r_id:

            mid_id = l_id+(r_id-l_id+1)/2
            mid_el = nums[mid_id]
            if target == mid_el:

                return mid_id
            if target > mid_el:
                l_id = mid_id+1

            if target < mid_el:
                r_id = mid_id-1
        if mid_id == 0 and target < mid_el:
            return 0

        return mid_id if nums[mid_id] > target and nums[mid_id-1] < target else mid_id+1

