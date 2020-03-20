# Problem Title: Repeated Substring Pattern
'''class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n<2: return False
        z_fn=[0]*n
        for i in range(1,n):
            j=0
            k=i
            while k<n and j<k and s[k] == s[j]:
                j+=1
                k+=1
            z_fn[i]=k-i
        for i in range(n):
            if z_fn[i]>0 and z_fn[i] == n-i and (n-i)%(i) == 0:
                return True

        return False'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        return (s[:]*2)[1:len(s)*2-1].find(s) != -1

