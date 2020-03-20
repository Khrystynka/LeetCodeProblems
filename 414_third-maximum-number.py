# Problem Title: Third Maximum Number
import bisect


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = []
        for el in nums:
            if len(max_list) < 3 and el not in max_list:
                bisect.insort(max_list, el)
                continue
            if el not in max_list:
                bisect.insort(max_list, el)
                if len(max_list) > 3:
                    max_list = max_list[1:]
        return max_list[len(max_list)-1] if len(max_list) < 3 else max_list[-3]

