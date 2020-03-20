# Problem Title: Backspace String Compare
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        res_S = []
        res_T = []
        for i in range(len(S)):
            if S[i] == '#':
                n = len(res_S)
                if n != 0:
                    res_S.pop()
            else:
                res_S.append(S[i])

        for i in range(len(T)):
            if T[i] == '#':
                n = len(res_T)
                if n != 0:
                    res_T.pop()
            else:
                res_T.append(T[i])
        return res_S == res_T

