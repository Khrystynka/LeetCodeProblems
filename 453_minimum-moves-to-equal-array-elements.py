# Problem Title: Minimum Moves to Equal Array Elements
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''Adding 1 to (n-1) elements is equivalent to subtracting 1 from one of the elements and adding 1 to all elements. Adding 1 to all elements does not change anything in terms of equality. So we must find the min number of (subtract 1 from any element) operations. The only way to make all elements equal this way is to make them all equal to the min element of the array.'''

        min_el = min(nums)
        res = sum([x-min_el for x in nums if x != min_el])
        return res

