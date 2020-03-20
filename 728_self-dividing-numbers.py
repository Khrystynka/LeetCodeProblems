# Problem Title: Self Dividing Numbers
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_selfdiv(num):
            if 0 < num < 10:
                return True
            original = num
            while num:
                digit = num % 10
                if digit == 0 or original % digit != 0:
                    return False
                num = num/10
            return True
        res = []
        for i in range(left, right+1):
            if is_selfdiv(i):
                res.append(i)
        return res

