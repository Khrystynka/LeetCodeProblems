# Problem Title: Pascal's Triangle II
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = [1]
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return prev_row
        for i in range(rowIndex):
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1]+prev_row[j])
            new_row.append(1)
            prev_row = new_row
            # print new_row
        return new_row

