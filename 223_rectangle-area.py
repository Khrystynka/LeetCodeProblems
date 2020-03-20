# Problem Title: Rectangle Area
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if C <= E or G <= A or D <= F or H <= B:
            overlap_area = 0
        else:
            x0 = max(A, E)
            x1 = min(C, G)
            y0 = max(F, B)
            y1 = min(H, D)
            overlap_area = abs(x0-x1)*abs(y0-y1)
        total_area = abs(A-C)*abs(D-B)+abs(G-E)*abs(H-F)
        # print total_area,overlap_area
        return total_area-overlap_area

