# Problem Title: Largest Triangle Area
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        n = len(points)

        def dist(point1, point2):
            return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

        def isvalidTriangle(a, b, c):
            return (a+b) > c and (a+c) > b and (c+b) > a

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    a = points[i]
                    b = points[j]
                    c = points[k]
                    area = abs(a[0]*(b[1] - c[1]) + b[0] *
                               (c[1] - a[1]) + c[0]*(a[1] - b[1])) / 2.0

                    max_area = max(max_area, area)

        return max_area

