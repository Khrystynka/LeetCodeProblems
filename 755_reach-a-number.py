# Problem Title: Reach a Number
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        total = 0
        k = 0
        while total < target:
            k += 1
            total += k
        delta = total-target
        if delta % 2 == 0:
            return k
        if (k+1) % 2:
            return k+1
        return k+2

