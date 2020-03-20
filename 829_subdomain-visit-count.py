# Problem Title: Subdomain Visit Count
from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = defaultdict(lambda: 0)
        for s in cpdomains:

            (count, domains) = s.split()
            count = int(count)
            domain_pieces = domains.split('.')
            i = len(domain_pieces)-1
            s = ''
            while i >= 0:
                s = domain_pieces[i]+('.' if s != '' else '')+s
                d[s] += count
                i -= 1
        res = []
        for key in d:
            res.append(str(d[key])+' '+str(key))
        return res

