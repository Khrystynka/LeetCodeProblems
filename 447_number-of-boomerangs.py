# Problem Title: Number of Boomerangs
from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = {}
        n = len(points)
        res = 0
        if n < 3:
            return res
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                dist = (points[i][0]-points[j][0])**2 + \
                    (points[i][1]-points[j][1])**2
                d[dist] = d.get(dist, 0) + 1

            for cnt in d.values():
                if cnt > 1:
                    res += cnt*(cnt-1)
            d = {}
        return res

