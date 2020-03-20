# Problem Title: Fraction to Recurring Decimal
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        remainder_dict = {}
        res = ''
        if numerator == 0:
            return '0'
        if numerator < 0:
            if denominator < 0:
                denominator = -denominator
            else:
                res += '-'
            numerator = -numerator
        elif denominator < 0:
            denominator = -denominator
            res += '-'
        res += str(numerator/denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return res
        res += '.'
        while remainder != 0:
            if remainder in remainder_dict:
                return res[:remainder_dict[remainder]]+"("+res[remainder_dict[remainder]:]+")"
            remainder_dict[remainder] = len(res)
            res += str(remainder*10/denominator)
            remainder = (remainder*10) % denominator
        return res

