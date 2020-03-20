# Problem Title: Contains Duplicate III
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        nums = sorted(zip(nums, range(n)))
        for i in range(n):
            j = i+1
            while j < n and abs(nums[i][0]-nums[j][0]) <= t:
                if abs(nums[i][1]-nums[j][1]) <= k:
                    return True
                j += 1
        return False

