# Problem Title: Word Search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])

        def dfs(i, j, word_left, board):
            if len(word_left) == 0:
                return True
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] == '1':
                return
            if board[i][j] == word_left[0]:
                temp = board[i][j]
                board[i][j] = '1'
                if dfs(i-1, j, word_left[1:], board) or dfs(i+1, j, word_left[1:], board) or dfs(i, j-1, word_left[1:], board) or dfs(i, j+1, word_left[1:], board):
                    return True
                board[i][j] = temp
                return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, word, board):
                    return True
        return False

