# Problem Title: Set Matrix Zeroes
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first_col = matrix[0][0]
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if j == 0:
                        first_col = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if first_col == 0:
            for i in range(n):
                matrix[i][0] = 0
        return matrix

