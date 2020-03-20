# Problem Title: ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ['']*numRows
        m = len(s)
        down = True
        row = 0
        for i in range(m):
            if row > numRows-1:
                down = False
                row = row-2
            elif row < 0:
                down = True
                row += 2
            res[row] += s[i]
            row = row + 1 if down else row - 1
        return ''.join(res)

