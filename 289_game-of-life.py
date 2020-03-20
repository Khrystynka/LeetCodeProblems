# Problem Title: Game of Life
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        neighbors = [[-1, -1], [-1, 0], [-1, 1],
                     [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]

        def neighbor_value(i, j, n, m, board):
            if i >= 0 and j >= 0 and i < n and j < m:
                return 1 if board[i][j] == 1 or board[i][j] == -2 else 0
            return 0

        for i in range(n):
            for j in range(m):
                suma = 0
                for neighbor in neighbors:
                    suma += neighbor_value(i +
                                           neighbor[0], j+neighbor[1], n, m, board)
                if board[i][j] == 1:
                    if suma < 2 or suma > 3:
                        board[i][j] = -2
                elif suma == 3:
                    board[i][j] = 2
        for i in range(n):
            for j in range(m):
                if board[i][j] == -2:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

