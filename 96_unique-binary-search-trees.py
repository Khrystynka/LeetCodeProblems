# Problem Title: Unique Binary Search Trees
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        memo[0] = 1
        memo[1] = 1

        def calcnum(k):
            if k in memo:
                return memo[k]
            else:
                res = 0
                for i in range(k):
                    res += calcnum(i)*calcnum(k-i-1)
                memo[k] = res
            return res
        return calcnum(n)

