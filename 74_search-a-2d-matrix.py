# Problem Title: Search a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        n = len(matrix)
        m = len(matrix[0])

        def toindexes(k, m):
            return (k/m, k % m)
        left = 0
        right = n*m-1
        mid = (left+right)/2
        while left <= right:
            (i, j) = toindexes(mid, m)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)/2
        return False

