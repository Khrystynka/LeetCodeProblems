# Problem Title: Island Perimeter
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if grid == [[]]:
            return res
        col_len = len(grid)
        row_len = len(grid[0])
        for i in range(col_len):
            for j in range(row_len):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j-1] == 0:
                        res += 1
                    if j == row_len-1 or grid[i][j+1] == 0:
                        res += 1
                    if i == 0 or grid[i-1][j] == 0:
                        res += 1
                    if i == col_len-1 or grid[i+1][j] == 0:
                        res += 1
        return res

