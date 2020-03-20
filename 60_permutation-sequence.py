# Problem Title: Permutation Sequence
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k-1  # k-th permutation starting from 0
       # https://www.techtud.com/short-notes/factorial-number-system
        res = []
        infactorialbase = []
        nums = []
        for l in range(1, n+1):
            nums.append(l)
        if k == 0:
            return ''.join(map(str, nums))
        i = 1
        while k != 0:
            infactorialbase.append(k % i)
            k = k/i
            i += 1
        infactorialbase = infactorialbase + [0]*(n-len(infactorialbase))
        for i in range(len(infactorialbase)-1, -1, -1):
            res.append(nums.pop(infactorialbase[i]))
        return ''.join(map(str, res))

