# Problem Title: Repeated String Match
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        k = (len(B)-1)/len(A)+1  # ceil k
        if B in A*k:
            return k
        if B in A*(k+1):
            return k+1
        return -1

