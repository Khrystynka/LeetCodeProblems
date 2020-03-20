# Problem Title: String to Integer (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = -1
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        def convert(s):
            i = 0
            num = 0
            minus = False
            if len(s) == 0:
                return 0
            if s[0] == '-' or s[0] == "+":
                minus = True if s[0] == '-' else False
                i = 1
            for i in range(i, len(s)):
                if s[i] not in d:
                    return 0
                num = num*10+d[s[i]]
            if minus:
                num = -(num) if -num > -2**31 else -2**31
            if num >= 2**31 - 1:
                return 2**31 - 1
            return num
        for i in range(len(str)):
            if str[i] == ' ' and start != -1:
                return convert(str[start:i])

            if str[i] != ' ' and str[i] != '-' and str[i] != '+' and not str[i].isdigit():
                if start != -1:
                    return convert(str[start:i])
                else:
                    return 0

            if str[i] == '-' or str[i] == '+':
                if start == -1:
                    start = i
                else:
                    return convert(str[start:i])

            if str[i].isdigit():
                if start == -1:
                    start = i
        return convert(str[start:])

