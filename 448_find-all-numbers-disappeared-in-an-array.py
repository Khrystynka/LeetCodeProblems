# Problem Title: Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0:
                nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


'''class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]jk
        :rtype: List[int]
        """
        n=len(nums)
        res=[]
        if nums == []:
            return nums
        for i in range(0,n):
            if nums[i] != i+1:
                j=i
                value=nums[j]
                while nums[j]!=j+1:
                    temp=nums[j]
                    nums[j]=value
                    value=temp
                    j=temp-1
        for i in range(0,n):
            if nums[i]!=i+1:
                res.append(i+1)

        return res'''

