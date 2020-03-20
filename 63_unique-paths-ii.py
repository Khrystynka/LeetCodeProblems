# Problem Title: Unique Paths II
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j] ^ 1
                elif i == 0:
                    obstacleGrid[i][j] = min(
                        obstacleGrid[i][j-1], obstacleGrid[i][j] ^ 1)
                elif j == 0:
                    obstacleGrid[i][j] = min(
                        obstacleGrid[i-1][j], obstacleGrid[i][j] ^ 1)
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

