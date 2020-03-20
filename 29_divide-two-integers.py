# Problem Title: Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_value = 2**31-1
        min_value = -2**31
        i = 0
        neg = False
        if dividend < 0:
            neg = True
            dividend = abs(dividend)
        if divisor < 0:
            neg = not neg
            divisor = abs(divisor)
        if dividend < divisor:
            return 0
        total_sum = 0
        total_quot = 0
        while (dividend-total_sum) >= divisor:
            suma = divisor
            quotient = 1
            remaining = dividend-total_sum
            while (remaining-(suma << 1)) >= 0:
                if total_quot+quotient >= max_value/2 and not neg:
                    return max_value
                if total_quot+quotient >= abs(min_value)/2 and neg:
                    return min_value
                quotient = quotient << 1
                suma = suma << 1
                # print 'quot', quotient,'suma',suma
            total_sum += suma
            total_quot += quotient
        return -total_quot if neg else total_quot

