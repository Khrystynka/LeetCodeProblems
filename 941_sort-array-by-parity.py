# Problem Title: Sort Array By Parity
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for el in A:
            if el % 2:
                odd.append(el)
            else:
                even.append(el)
        return even+odd

