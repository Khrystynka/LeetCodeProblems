# Problem Title: Magic Squares In Grid
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        a = grid

        def ismagic(arr):
            if len(arr) != len(set(arr)):
                return False
            for i in range(len(arr)):
                if arr[i] not in range(1, 10):
                    return False
            if sum(arr[:3]) != sum(arr[3:6]) or sum(arr[:3]) != sum(arr[6:9]) or (arr[0]+arr[4]+arr[8]) != (arr[2]+arr[4]+arr[6]) or (arr[0]+arr[4]+arr[8]) != sum(arr[:3]) or (arr[0]+arr[3]+arr[6]) != sum(arr[:3]):
                return False
            return True

        for i in range(row_cnt-2):
            for j in range(col_cnt-2):
                if ismagic([a[i][j], a[i][j+1], a[i][j+2], a[i+1][j], a[i+1][j+1], a[i+1][j+2], a[i+2][j], a[i+2][j+1], a[i+2][j+2]]):
                    res += 1
        return res

