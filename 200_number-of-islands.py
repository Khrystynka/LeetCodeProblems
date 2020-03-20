# Problem Title: Number of Islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.n = len(grid)
        count = 0
        if self.n == 0:
            return 0
        self.m = len(grid[0])

        def dfs(self, i, j):
            if i >= self.n or j >= self.m or i < 0 or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(self, i+1, j)
            dfs(self, i-1, j)
            dfs(self, i, j+1)
            dfs(self, i, j-1)
        for i in range(self.n):

            for j in range(self.m):
                if grid[i][j] == '1':
                    dfs(self, i, j)
                    count += 1

        return count

