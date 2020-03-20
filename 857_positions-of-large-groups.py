# Problem Title: Positions of Large Groups
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        prev_ind = 0
        i = 1
        res = []
        while i < len(S):
            while i < len(S) and S[i] == S[prev_ind]:
                i = i+1
            if i-prev_ind >= 3:
                res.append([prev_ind, i-1])
            prev_ind = i
            i += 1

        return res

