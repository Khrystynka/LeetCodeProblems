# Problem Title: Convert a Number to Hexadecimal
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = ''
        d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
             8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num > 0:
            while num != 0:
                res += d[num % 16]
                num = num/16

            return res[::-1]
        if num < 0:
            # convert to binary and for each bit substitute 0 with 1 and 1 with 0 and add one
            num = abs(num)
            bin_two_comp = [1]*32
            i = 1
            while num != 0:
                bin_two_comp[-i] = 1-num % 2
                num = num/2
                i += 1
            # add one to binary with reversed bits
            print bin_two_comp
            carry = 1
            i = 1
            while i <= 32 and carry:
                temp = (bin_two_comp[-i]+carry) % 2
                bin_two_comp[-i] = (bin_two_comp[-i]+carry) % 2
                carry = 1-temp
                i += 1
            i = 0
            print bin_two_comp
            while i < 32:
                res += str(d[bin_two_comp[i]*2**3+bin_two_comp[i+1]
                             * 2**2+bin_two_comp[i+2]*2**1+bin_two_comp[i+3]*1])
                i = i+4
            return res

