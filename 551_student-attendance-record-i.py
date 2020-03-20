# Problem Title: Student Attendance Record I
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA = 0
        for l in range(len(s)):
            if s[l] == 'A':
                countA += 1
                if countA >= 2:
                    return False
            if s[l] == 'L'and s[l:l+3] == 'LLL':
                return False
        return True

