# Problem Title: Different Ways to Add Parentheses
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.dp = {}

        def evalexpr(op, a, b):
            if op == '+':
                return (a)+(b)
            if op == '-':
                return (a)-(b)
            if op == '*':
                return (a)*(b)

        def ways_to_interpret(expr):
            res = []
            if expr in self.dp:
                return self.dp[expr]
            if '+' not in expr and '-'not in expr and '*' not in expr:
                return [int(expr)]
            for i in range(len(expr)):
                if expr[i] == '+' or expr[i] == '-' or expr[i] == '*':
                    leftside = ways_to_interpret(expr[:i])
                    rightside = ways_to_interpret(expr[i+1:])
                    for num1 in leftside:
                        for num2 in rightside:
                            res.append(evalexpr(expr[i], num1, num2))
            self.dp[expr] = res
            return res
        return ways_to_interpret(input)

