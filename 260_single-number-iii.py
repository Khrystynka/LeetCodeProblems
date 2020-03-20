# Problem Title: Single Number III
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        suma = 0
        partsum = 0
        mask = 1
        for i in range(len(nums)):
            suma = suma ^ nums[i]
        while suma & mask != mask:
            mask = mask << 1
        for i in range(len(nums)):
            if nums[i] & mask == mask:
                partsum ^= nums[i]
        return [partsum, suma ^ partsum]

