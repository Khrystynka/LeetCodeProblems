# Problem Title: Largest Number At Least Twice of Others
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_el = nums[0]
        ind = 0
        second_max = float('-inf')
        for i in range(1, len(nums)):
            if nums[i] > max_el:
                second_max = max_el
                max_el = nums[i]
                ind = i
            elif nums[i] > second_max:
                second_max = nums[i]
       # print max_el,second_max
        return ind if second_max*2 <= max_el else -1

