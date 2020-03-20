# Problem Title: Combination Sum III
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n > 9*k:
            return res

        def dfs(curr_res, ind, target):
            # print curr_res, ind,target
            if target == 0 and len(curr_res) == k:
                res.append(curr_res)
                return
            if target <= 0 or len(curr_res) == k:
                return
            for i in range(ind, min(n+1, 10)):
                dfs(curr_res+[i], i+1, target-i)
        dfs([], 1, n)
        return res

