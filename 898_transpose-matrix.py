# Problem Title: Transpose Matrix
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row_cnt = len(A)
        col_cnt = len(A[0])
        B = []
        for i in range(col_cnt):
            row = []
            for j in range(row_cnt):

                row.append(A[j][i])
            B.append(row)
        return B

