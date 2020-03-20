# Problem Title: Restore IP Addresses
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()

        def generateIP(sofar='', s_remaining=s, num_remaining=4):
            if s_remaining == '' and num_remaining == 0:
                res.add(sofar[:-1])
            if s_remaining == '' or num_remaining == 0:
                return
            generateIP(sofar+s_remaining[0]+'.',
                       s_remaining[1:], num_remaining-1)
            if s_remaining[0] != '0':
                generateIP(sofar+s_remaining[0:2]+'.',
                           s_remaining[2:], num_remaining-1)
                if int(s_remaining[:3]) <= 255:
                    generateIP(
                        sofar+s_remaining[0:3]+'.', s_remaining[3:], num_remaining-1)
        generateIP()
        return res

