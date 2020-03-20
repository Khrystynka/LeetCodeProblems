# Problem Title: Combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(start, n, k, comb=[]):
            if k == 0:
                self.res.append(comb)
                return self.res
            while start <= n:
                dfs(start+1, n, k-1, comb+[start])
                start = start+1

        dfs(1, n, k)
        return self.res

