# Problem Title: Shortest Unsorted Continuous Subarray
'''class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        nums2=sorted(nums)
        n=len(nums)
        start=-1
        end=-1
        i=0
        while i<=n-1:
            if start==-1 and nums[i]!=nums2[i]:
                start=i
            if end==-1 and nums[n-i-1]!=nums2[n-i-1]:
                end=n-i
            i+=1
            #print start,end
            
            if end!=-1 and start!=-1:
                return end-start
        return 0'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        if nums == []:
            return 0
        n = len(nums)
        max_el = nums[0]
        min_el = nums[n-1]
        end = -1
        start = -1
        for i in range(1, n):
            if nums[i] >= max_el:
                max_el = nums[i]
            else:
                end = i
        for i in range(n-2, -1, -1):
            if nums[i] <= min_el:
                min_el = nums[i]
            else:
                start = i
        return end-start if end <= start else end-start+1

