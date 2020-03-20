# Problem Title: Combination Sum
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()  # make sure break is no needed in further loop

        def combination(pre_val, candidates, target):
            for i, c in enumerate(candidates):
                if target - c == 0:
                    res.append(pre_val + [c])
                elif target - c > 0:
                    combination(pre_val + [c], candidates[i:], target - c)
                else:
                    break  # break when target is negative
        combination([], candidates, target)
        return res

