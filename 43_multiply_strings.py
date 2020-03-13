__author__ = 'khrystyna'
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        lst1 = list(map(int, num1))
        lst2 = list(map(int, num2))
        n = len(lst1)
        m = len(lst2)
        res = [0 for _ in range(n+m-1)]
        for j in range(m):
            for i in range(n):
                res[i+j] += lst1[i] * lst2[j]
        carry = 0
        for i in range(len(res)-1,-1,-1):
            carry, res[i] = divmod(res[i] + carry, 10)
        if carry:
            res = [carry] + res
        return ''.join(map(str, res))

if __name__ == '__main__':
    assert(Solution().multiply('123', '456') == '56088')


