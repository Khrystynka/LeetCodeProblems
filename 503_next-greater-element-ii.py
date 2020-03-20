# Problem Title: Next Greater Element II
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return [-1]*n
        stack = [(nums[0], 0)]
        res = [-1]*n
        p1 = 1
        p2 = None
        while stack != [] and p1 != stack[-1][1]:

            while nums[p1] <= stack[-1][0] and p1 != stack[-1][1]:
                if stack[-1][1] < p1:
                    stack.append((nums[p1], p1))
                p1 = (p1+1) % n
            while stack and nums[p1] > stack[-1][0]:
                (elem, p2) = stack.pop()
                res[p2] = nums[p1]
            if stack == [] or p1 > stack[-1][1]:
                stack.append((nums[p1], p1))
                p1 = (p1+1) % n
        # if not stack:
        return res

