# Problem Title: Triangle
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(1, n):
            k = len(triangle[i])
            for j in range(k):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == k-1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[n-1])

