# Problem Title: Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits)-1
        new_digit = digits[i]+1
        while new_digit % 10 == 0 and i > 0:
            digits[i] = 0
            i = i-1
            new_digit = digits[i]+1
        if new_digit == 10:
            digits[i] = 0
            return [1]+digits
        digits[i] = new_digit
        return digits

