# Problem Title: Add Strings
class Solution(object):
    def addStrings(self, num1, num2):
        _str = ""
        carr = 0
        i = len(num1)-1
        j = len(num2)-1
        if j > i:
            i, j = j, i
            num1, num2 = num2, num1
        while i > -1:
            if j > -1:
                val = ord(num1[i])-48 + ord(num2[j])-48 + carr
                j -= 1
            else:
                val = ord(num1[i])-48 + carr
            carr = val/10
            _str = str(val % 10)+_str
            i -= 1

        if carr > 0:
            _str = str(carr)+_str

        return _str

