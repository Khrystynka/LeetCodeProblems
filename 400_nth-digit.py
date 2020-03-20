# Problem Title: Nth Digit
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        i = 0
        n1 = n
        count = 0
        while n1 > 0:
            n1_prev = n1
            count_prev = count
            temp = (i+1)*9*10**i
            n1 = n1-temp
            count += 9*10**i
            i += 1
        digit_count = i
        res = count_prev+(n1_prev/digit_count)
        index = n1_prev % digit_count
        if index == 0:
            return res % 10
        res += 1
        return str(res)[index-1]

