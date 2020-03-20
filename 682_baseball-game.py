# Problem Title: Baseball Game
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for op in ops:
            if op == "D":
                points.append(points[-1]*2)
            elif op == '+':
                points.append(points[-1] if len(points) ==
                              1 else points[-1]+points[-2])
            elif op == "C":
                points.pop()
            else:
                points.append(int(op))
        return sum(points)

