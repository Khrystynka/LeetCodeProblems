# Problem Title: Count Primes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        lst = [True]*(n)
        lst[0] = False
        lst[1] = False
        i = 2
        while i*i <= n:
            if lst[i] == True:
                for j in range(i*i, n, i):
                    lst[j] = False
            i += 1
        return sum(lst)

