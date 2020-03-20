# Problem Title: Rotated Digits
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 9: 6, 8: 8}
        count = 0

        def isvalid(number):
            p = False
            while number:
                digit = number % 10
                if digit not in d:
                    return False
                if digit != d[digit]:
                    p = True
                number = number/10
            return p

        for number in range(1, N+1):
            if isvalid(number):
                count += 1
        return count

