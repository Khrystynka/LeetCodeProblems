# Problem Title: Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                if stack == [] or d[stack.pop()] != char:
                    return False
        return stack == []

