# Problem Title: Reshape the Matrix
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        res = []
        row = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):

                row.append(nums[i][j])
                count += 1
                if count % c == 0:
                    res.append(row)
                    count = 0
                    row = []
        return res

