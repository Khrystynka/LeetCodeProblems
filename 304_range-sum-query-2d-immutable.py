# Problem Title: Range Sum Query 2D - Immutable
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.accum = [[matrix[i][j]
                       for j in range(len(matrix[0]))]for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0 and i == 0:
                    continue
                if j == 0:
                    self.accum[i][j] += self.accum[i-1][j]
                elif i == 0:
                    self.accum[i][j] += self.accum[i][j-1]
                else:
                    self.accum[i][j] += self.accum[i][j-1] + \
                        self.accum[i-1][j]-self.accum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.accum[row2][col2]
        if row1 == 0:
            return self.accum[row2][col2]-self.accum[row2][col1-1]
        elif col1 == 0:
            return self.accum[row2][col2]-self.accum[row1-1][col2]
        else:
            return self.accum[row2][col2]-self.accum[row1-1][col2]-self.accum[row2][col1-1]+self.accum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

