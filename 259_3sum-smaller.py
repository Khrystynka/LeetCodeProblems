# Problem Title: 3Sum Smaller
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        if n < 3:
            return 0
        res = sorted(nums)
        for p1 in range(0, n-2):
            p2 = p1+1
            p3 = n-1
            while p3 > p2:
                if res[p2]+res[p3] < target-res[p1]:
                    count += p3-p2
                    p2 += 1
                else:
                    p3 -= 1
        return count

