# Problem Title: Permutations II
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []

        def perm(perm_sofar, candidates):
            if candidates == []:
                res.append(perm_sofar)
                return
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i-1]:
                    continue
                perm(perm_sofar+[candidates[i]],
                     candidates[:i]+candidates[i+1:])
        perm([], nums)
        return res

