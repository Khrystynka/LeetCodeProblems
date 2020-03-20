# Problem Title: Hamming Distance
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        counting = False
        while z != 0:
            if z & 1 == 1:
                count += 1
            z = z >> 1
        return count

