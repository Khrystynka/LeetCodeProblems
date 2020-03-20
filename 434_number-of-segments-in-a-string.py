# Problem Title: Number of Segments in a String
class Solution(object):
    def countSegments(self, s):
        if s == '':
            return 0
        prev = ''
        count = 0
        for i in range(1, len(s)):

            if s[i] == ' ' and s[i-1] != '' and s[i-1] != ' ':
                count += 1
        if s[-1] != ' ':
            count += 1
        return count

