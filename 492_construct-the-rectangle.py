# Problem Title: Construct the Rectangle
from math import sqrt


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        i = 1
        L = 0
        W = 0

        while i <= sqrt(area):

            if area % i == 0:
                W = i
                L = area/W
            i += 1
        return [L, W]

