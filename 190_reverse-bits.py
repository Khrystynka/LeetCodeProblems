# Problem Title: Reverse Bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        i = 0
        while n:
            last_bit = n & 1
            res = res*2+last_bit
            n = n >> 1
            i += 1
        res = res*(2**(32-i))
        return res

