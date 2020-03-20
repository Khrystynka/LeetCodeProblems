# Problem Title: Image Smoother
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row_count = len(M)
        col_count = len(M[0])

        res_array = [[-1 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(row_count):
            for j in range(col_count):
                res = 0
                count = 0
                for row in range(max(0, i-1), min(row_count, i+2)):
                    for col in range(max(0, j-1), min(col_count, j+2)):
                        res += M[row][col]
                        count += 1
                res_array[i][j] = res/count
        return res_array

