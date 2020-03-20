# Problem Title: Count and Say
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(1, n):
            p1 = 0
            new_s = ''

            while p1 < len(s):
                first_el = s[p1]
                p2 = p1+1
                while p2 < len(s) and s[p2] == first_el:
                    p2 += 1
                new_s = new_s+str(p2-p1)+first_el
                p1 = p2
            s = new_s
        return s

