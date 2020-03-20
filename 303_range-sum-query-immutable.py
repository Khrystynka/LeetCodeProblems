# Problem Title: Range Sum Query - Immutable
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums == []:
            cumul_sums = [0]
        else:
            self.cumul_sums = [0]*len(nums)
            self.cumul_sums[0] = nums[0]
            for i in range(1, len(nums)):
                self.cumul_sums[i] = self.cumul_sums[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.cumul_sums[j]-self.cumul_sums[i-1] if i > 0 else self.cumul_sums[j]

