# Problem Title: Factor Combinations
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def possible_factors(n):
            res = [[n]]
            k = 2
            while (k*k <= (n)):
                if n % k == 0:
                    rightside = possible_factors(n/k)
                    for lst in rightside:
                        if lst[0] >= k:
                            res.append([k]+lst)
                k += 1
            return res
        k = 2
        while k*k <= (n):
            if n % k == 0:
                rightside = possible_factors(n/k)
                for el in rightside:
                    if el[0] >= k:
                        res.append([k]+el)
            k += 1
        return res

