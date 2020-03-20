# Problem Title: Max Consecutive Ones
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        max_sofar = 0
        current = 0
        for el in nums:
            if el == 1:
                current += 1
            else:
                if current > max_sofar:
                    max_sofar = current
                current = 0
        return max(max_sofar, current)

