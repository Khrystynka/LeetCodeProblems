# Problem Title: Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        op = set(['+', '-', '*', '/'])

        def calc(op, op1, op2):
            op1 = int(op1)
            op2 = int(op2)
            if op == "+":
                return (op1)+(op2)
            if op == "-":
                return (op1)-(op2)
            if op == "/":
                if op1 == 0:
                    return 0
                if (op1 < 0 and op2 < 0) or (op1 > 0 and op2 > 0):
                    minus = False
                else:
                    minus = True
                return -(abs(op1)/abs(op2)) if minus else op1/op2
            if op == "*":
                return int(op1)*int(op2)

        for token in tokens:
            if token in op:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(calc(token, op1, op2))
            else:
                stack.append(token)
            # print stack
        return stack[-1]

