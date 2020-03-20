# Problem Title: Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n < 1:
            return []
        m = len(matrix[0])
        res = []

        def outer(rc, n, m):
            if n <= 0 or m <= 0:
                return
            for j in range(m):
                res.append(matrix[rc][rc+j])
            for i in range(1, n):
                res.append(matrix[rc+i][rc+m-1])
            if n > 1:
                for j in range(m-2, -1, -1):
                    res.append(matrix[rc+n-1][rc+j])
            if m > 1:
                for i in range(n-2, 0, -1):
                    res.append(matrix[rc+i][rc])

        for k in range(len(matrix)/2+1):
            outer(k, n, m)
            n = n-2
            m = m-2
        return res

