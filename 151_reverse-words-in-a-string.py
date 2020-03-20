# Problem Title: Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        words = s.split()
        for i in range(len(words)-1, -1, -1):
            res += words[i]+' '
        return res[:-1]

