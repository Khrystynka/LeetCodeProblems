# Problem Title: Search a 2D Matrix II
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        starti = n-1
        startj = 0
        # print starti,startj,n,m
        while starti >= 0 and startj >= 0 and starti < n and startj < m:
            elem = matrix[starti][startj]
            if elem == target:
                return True
            if elem > target:
                starti -= 1
            else:
                startj += 1
        return False

