# Problem Title: License Key Formatting
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ''
        j = 0
        S_arr = []
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                if j < K:
                    res += S[i].upper()
                    j += 1
                else:
                    S_arr.append(res[::-1])
                    j = 1
                    res = S[i].upper()
        if len(res) >= 1:
            S_arr.append(res[::-1])
        return '-'.join(S_arr[::-1])

