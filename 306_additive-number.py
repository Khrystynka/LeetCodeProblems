# Problem Title: Additive Number
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def next_number(s1, s2):
            if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                return ''
            return str(int(s1)+int(s2))

        def possible(num):
            for i in range(len(num)-2):
                for j in range(i+1, len(num)-1):
                    res = next_number(num[:i+1], num[i+1:j+1])
                    if res != ''and res == num[j+1:j+1+len(res)]:
                        num1 = num[i+1:j+1]
                        num2 = num[j+1:j+1+len(res)]
                        if check(num1, num2, j+1+len(res)):
                            return True
            return False

        def check(num1, num2, k):
            while k < len(num):
                res = next_number(num1, num2)
                if res == '' or res != num[k:k+len(res)]:
                    return False
                k = k+len(res)
                num1 = num2
                num2 = res
            return True
        return possible(num)

