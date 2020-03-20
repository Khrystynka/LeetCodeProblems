# Problem Title: Basic Calculator II
class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        op = ['+', '-', '*', '/']
        if s == '':
            return 0
        sign = ''
        number = 0
        for char in s+'+':
            if char.isalnum():
                number = number*10+int(char)
            elif char in op:
                if sign == '':
                    stack.append(number)
                elif sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    first_int = stack.pop()
                    stack.append(first_int*number)
                elif sign == '/':
                    first_int = stack.pop()

                    stack.append(first_int/number if first_int >
                                 0 else (-1)*(abs(first_int)/number))
                sign = char
                number = 0
        return sum(stack)

