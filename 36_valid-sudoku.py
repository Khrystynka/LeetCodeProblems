# Problem Title: Valid Sudoku
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        rows = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        boxes = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el != '.':
                    if el in rows[i] or el in columns[j] or el in boxes[(i/3)*3+j/3]:
                        return False
                    else:
                        rows[i][el] = 1
                        columns[j][el] = 1
                        boxes[(i/3*3+j/3)][el] = 1
        return True

