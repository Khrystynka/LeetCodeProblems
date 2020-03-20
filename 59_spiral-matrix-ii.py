# Problem Title: Spiral Matrix II
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        next_number = 1

        def fill_outer(start, next_number, n):
            for j in range(start, start+n):
                matrix[start][j] = next_number
                next_number += 1
            for i in range(start+1, start+n):
                matrix[i][start+n-1] = next_number
                next_number += 1
            for j in range(start+n-2, start-1, -1):
                matrix[start+n-1][j] = next_number
                next_number += 1
            for i in range(start+n-2, start, -1):
                matrix[i][start] = next_number
                next_number += 1
            return next_number
        k = n/2
        for i in range(k+1):
            next_number = fill_outer(i, next_number, n)
            n = n-2
        return matrix

