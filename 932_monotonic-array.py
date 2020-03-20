# Problem Title: Monotonic Array
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def isinc(a):
            for i in range(len(a)-1):
                if a[i] > a[i+1]:
                    return False
            return True

        def decr(a):
            for i in range(len(a)-1):
                if a[i] < a[i+1]:
                    return False
            return True
        return isinc(A) or decr(A)

