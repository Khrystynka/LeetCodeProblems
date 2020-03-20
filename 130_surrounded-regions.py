# Problem Title: Surrounded Regions
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == []:
            return board
        self.n = len(board)
        self.m = len(board[0])

        def successors(i, j):
            res = []
            if j-1 >= 0 and board[i][j-1] == 'O':
                res.append((i, j-1))
            if j+1 < self.m and board[i][j+1] == 'O':
                res.append((i, j+1))
            if i-1 >= 0 and board[i-1][j] == 'O':
                res.append((i-1, j))
            if i+1 < self.n and board[i+1][j] == 'O':
                res.append((i+1, j))
            return res

        def dfs(i, j):
            board[i][j] = '*'
            for (r, c) in successors(i, j):
                dfs(r, c)
        for i in range(self.n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][self.m-1] == 'O':
                dfs(i, self.m-1)
        for j in range(1, self.m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[self.n-1][j] == 'O':
                dfs(self.n-1, j)
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

