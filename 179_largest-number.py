# Problem Title: Largest Number
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def func(x, y):
            if int(str(x)+str(y)) > int(str(y)+str(x)):
                return -1
            elif int(str(x)+str(y)) < int(str(y)+str(x)):
                return 1
            else:
                return 0
        func = cmp_to_key(func)
        ans = [str(x) for x in (sorted(nums, key=func))]
        i = 0
        while ans[i] == "0" and i < len(nums)-1:
            i += 1
        return "".join(ans[i:])

