# Problem Title: Perfect Number
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        res = 0
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                res += i + num/i
                if res > num:
                    return False
        return True if res+1 == num else False

