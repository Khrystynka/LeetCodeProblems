# Problem Title: Range Sum Query - Mutable
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.accum = []
        for i in range(len(nums)):
            if i == 0:
                self.accum.append(self.nums[i])
            else:
                self.accum.append(self.accum[-1]+self.nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        mod = val-self.nums[i]
        self.nums[i] = val
        for k in range(i, len(self.accum)):
            self.accum[k] += mod

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accum[j]-self.accum[i-1] if i != 0 else self.accum[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

