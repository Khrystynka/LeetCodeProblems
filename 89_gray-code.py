# Problem Title: Gray Code
class Solution(object):
    def grayCode(self, n):
        """Let's summarize results for N = 3:
000 (level 0)
001 (level 1)
011 (level 2)
010
110 (level 3)
111
101
100

level 1 is just reverse tracking level 0 and add 001 (or 1 << 0).
level 2 is just reverse tracking level 0,1 and add 010 ( or 1 << 1).
level 3 is just reverse tracking level 0,1,2 and add 100 (or 1 << 2)

You can think level N is the mirrored results of level 0,...,N-1 and add bit (1 << (N-1))
level 0,...,N as whole will be the gray code for n = N


        :type n: int
        :rtype: List[int]
        """
        res = [0]
        k = 0
        while k < n:
            for el in res[::-1]:
                res.append(el | 1 << k)
            k += 1
        return res

