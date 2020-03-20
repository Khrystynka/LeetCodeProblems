# Problem Title: Prime Number of Set Bits in Binary Representation
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # 1number == 32 bits, so max prime number of set bits <32
        prime_set = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        res = 0
        for number in range(L, R+1):
            count = 0
            while number:
                count += number & 1
                number = number >> 1
            if count in prime_set:
                res += 1
        return res

