# Problem Title: Find the Duplicate Number
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # detect intersection of tortuise and a heair pointers
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        p1 = 0
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

