# Problem Title: Missing Ranges
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        self.res = []
        if nums == []:
            return [(str(lower)+'->'+str(upper))] if upper != lower else[str(lower)]
        if lower != nums[0]:
            nums = [lower-1]+nums
        if upper != nums[-1]:
            nums += [upper+1]
        n = len(nums)-1
        print nums

        def fill_gap(left, right):
            if right > n:
                return
            if nums[left]+1 < nums[right]:
                if nums[left] == nums[right]-2:
                    self.res.append(str(nums[left]+1))
                else:
                    self.res.append(str(nums[left]+1)+'->'+str(nums[right]-1))
            fill_gap(right, right+1)
        fill_gap(0, 1)
        return self.res

