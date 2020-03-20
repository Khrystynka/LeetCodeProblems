# Problem Title: Walls and Gates
from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        if n == 0:
            return
        m = len(rooms[0])
        queu = deque()
        next_moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queu.append((i, j))
        while queu:
            (row, col) = queu.popleft()
            for move in next_moves:
                r = row+move[0]
                c = col+move[1]
                if r < 0 or r >= n or c < 0 or c >= m or rooms[r][c] != 2147483647:
                    continue
                rooms[r][c] = rooms[row][col]+1
                queu.append((r, c))

