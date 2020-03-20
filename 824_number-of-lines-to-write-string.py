# Problem Title: Number of Lines To Write String
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        total = 0
        lines = 0

        for letter in S:
            temp = total+widths[ord(letter)-ord('a')]
            if temp > 100:
                total = widths[ord(letter)-ord('a')]
                lines += 1
            else:
                total = temp

        return [lines+1 if total != 0 else lines, total]

