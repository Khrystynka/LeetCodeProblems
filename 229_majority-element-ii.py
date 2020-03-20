# Problem Title: Majority Element II
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return nums
        n = len(nums)
        cand1 = None
        vote1 = 0
        cand2 = None
        vote2 = 0
        res = []
        for i in range(n):
            if nums[i] == cand1:
                vote1 += 1
            elif nums[i] == cand2:
                vote2 += 1
            elif vote1 == 0:
                cand1 = nums[i]
                vote1 = 1
            elif vote2 == 0:
                cand2 = nums[i]
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        vote1 = 0
        vote2 = 0
        for i in range(n):
            if cand1 == nums[i]:
                vote1 += 1
            elif cand2 == nums[i]:
                vote2 += 1
        if vote1 > (n/3):
            res.append(cand1)
        if vote2 > n/3:
            res.append(cand2)
        return res

