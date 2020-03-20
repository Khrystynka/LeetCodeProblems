# Problem Title: Move Zeroes
"""class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        if nums==[]: return []
        while i<len(nums):
            while i<len(nums) and nums[i]!=0:
                i+=1
            if j<=i:
                j=i+1
            while j<len(nums) and nums[j] == 0:
                j+=1
            if j<len(nums):
                nums[i]=nums[j]
                nums[j]=0
                i=i+1
                j=j+1
            if j>=len(nums):

                for k in range(i,len(nums)):
                    nums[k]=0
                return nums
"""


class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)
        while i < n and nums[i] != 0:
            i += 1
        for j in range(i, n):
            if nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
        return nums

