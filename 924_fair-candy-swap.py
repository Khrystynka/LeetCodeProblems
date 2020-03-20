# Problem Title: Fair Candy Swap
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum1 = sum(A)
        sum2 = sum(B)
        setB = set(B)
        target = (sum1+sum2)/2
        for el1 in A:
            el2 = target - (sum1-el1)
            if el2 > 0 and el2 in setB:
                return [el1, el2]

