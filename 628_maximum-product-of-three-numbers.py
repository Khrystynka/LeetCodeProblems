# Problem Title: Maximum Product of Three Numbers
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return None
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')
        for el in nums:
            if el < min1:
                min2 = min1
                min1 = el
            elif el < min2:
                min2 = el
            if el >= max1:
                max3 = max2
                max2 = max1
                max1 = el
            elif el >= max2:
                max3 = max2
                max2 = el
            elif el > max3:
                max3 = el
        print max1, max2, max3, min2, min1
        return max(max3*max2*max1, max1*min1*min2)

