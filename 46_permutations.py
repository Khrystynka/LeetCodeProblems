# Problem Title: Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def buildPerm(permsofar, candidates):
            if candidates == []:
                res.append(permsofar)
                return
            for i, el in enumerate(candidates):
                buildPerm(permsofar+[candidates[i]],
                          candidates[:i]+candidates[i+1:])
        buildPerm([], nums)
        return res

