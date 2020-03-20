# Problem Title: Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        prev_line = [1, 1]
        for i in range(3, numRows+1):
            new_line = [1]
            for j in range(len(prev_line)-1):
                new_line.append(prev_line[j]+prev_line[j+1])
            new_line.append(1)
            res.append(new_line)
            prev_line = new_line
        return res

