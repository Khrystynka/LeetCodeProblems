# Problem Title: Maximal Square
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        maxlen = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                    maxlen = max(maxlen, matrix[i][j])
                elif matrix[i][j] == '1':
                    matrix[i][j] = min(
                        matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])+1
                    maxlen = max(maxlen, matrix[i][j])
                else:
                    matrix[i][j] = 0
        return maxlen**2

