# Problem Title: Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if len(s) == 0:
            return 0
        return len(s[-1])
