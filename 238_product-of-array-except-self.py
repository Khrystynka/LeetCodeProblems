# Problem Title: Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prod1 = [0]*n
        prod2 = [0]*n

        prod1[0] = 1
        prod2[n-1] = 1
        for i in range(n-1):
            prod1[i+1] = prod1[i]*nums[i]
            prod2[n-1-i-1] = prod2[n-1-i]*nums[n-1-i]
        for i in range(n):
            prod1[i] = prod1[i]*prod2[i]
        return prod1

