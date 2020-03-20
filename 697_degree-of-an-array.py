# Problem Title: Degree of an Array
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        degree = 0
        pos = []
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        for key in d.keys():
            if len(d[key]) > degree:
                degree = len(d[key])
                pos = [(d[key])]
            elif len(d[key]) == degree:
                pos.append(d[key])
        print d, pos
        return min([max(el)-min(el)+1 for el in pos])

