# Problem Title: Uncommon Words from Two Sentences
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        d = {}
        d = {}
        res = []
        for word in A.split(' '):
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        for word in B.split(' '):
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        for key in d:
            if d[key] == 1:
                res.append(key)
        return res

