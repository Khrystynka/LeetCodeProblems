# Problem Title: Next Permutation
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n-1
        while k > 0:
            if nums[k] <= nums[k-1]:
                k = k-1
            else:
                j = n-1
                while nums[j] <= nums[k-1]:
                    j -= 1

                nums[j], nums[k-1] = nums[k-1], nums[j]

                break
        nums[k:] = sorted(nums[k:])

