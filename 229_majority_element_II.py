__author__ = 'khrystyna'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = None
        cand2 = None
        vote1 = 0
        vote2 = 0
        res=[]
        for num in nums:
            if cand1 == num:
                vote1 += 1
            elif cand2 == num:
                vote2 += 1
            elif vote1 == 0:
                cand1 = num
                vote1 = 1
            elif vote2 == 0:
                cand2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        vote1, vote2 = 0, 0
        for num in nums:
            if cand1 == num:
                vote1 += 1
            elif cand2 == num:
                vote2 += 1
        if vote1 > len(nums)/3:
            res.append(cand1)
        if vote2 > len(nums)/3:
            res.append(cand2)
        return res

if __name__ == '__main__':
    assert(Solution().majorityElement([1,1,1,3,3,2,2,2]) == [1,2])