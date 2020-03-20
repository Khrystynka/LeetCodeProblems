# Problem Title: Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        res = []
        for s in strs:
            s_sorted = ''.join(sorted(s))
            # print s_sorted,s
            if s_sorted in d:
                d[s_sorted].append(s)
                # print d
            else:
                d[s_sorted] = [s]
        for key in d:
            res.append(d[key])
        return res

