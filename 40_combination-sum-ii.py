# Problem Title: Combination Sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []

        def comb(comb_so_far, new_target, candidates):
            # print candidates
            for i, el in enumerate(candidates):
                if i != 0 and candidates[i] == candidates[i-1]:
                    continue
                if new_target-el == 0:
                    res.append(comb_so_far+[el])
                if new_target-el <= 0:
                    break
                else:
                    comb(comb_so_far+[el], new_target-el, candidates[i+1:])
        comb([], target, candidates)
        return res

