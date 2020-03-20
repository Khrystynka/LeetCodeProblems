# Problem Title: Decode Ways
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = map(int, s)
        p_1 = 1
        res = 1
        for i in range(len(lst)):
            p_2 = p_1
            p_1 = res
            if lst[i] == 0:
                if i == 0 or lst[i-1] > 2 or lst[i-1] == 0:
                    return 0
                else:
                    res = p_2
            else:
                res = p_1
            if i != 0 and lst[i] > 0 and (lst[i-1] == 1 or (lst[i-1] == 2 and lst[i] <= 6)):
                res += p_2

        return res

