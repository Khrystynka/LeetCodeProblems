# Problem Title: Shortest Distance to a Character
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [-1]*n
        prev = float('-inf')

        for i in range(n):
            if S[i] == C:
                after = i
                for j in range(max(0, prev+1), i):
                    res[j] = min(j-prev, after-j)
                res[i] = 0
                prev = i
        if prev < n:
            for j in range(max(0, prev+1), n):
                res[j] = j-prev
        return res

