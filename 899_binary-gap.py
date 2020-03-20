# Problem Title: Binary Gap
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_dist = 0
        dist = 0
        while N:
            if N & 1 == 0:

                dist += 1 if dist != 0 else 0
            else:
                max_dist = max(max_dist, dist)
                dist = 1
            N = N >> 1
        return max_dist

